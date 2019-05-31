from django.shortcuts import render,redirect,get_object_or_404
from .models import Assignment,AssignmentUser
from .forms import AssignmentForm, SubmissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    assignment = Assignment.objects.all().order_by('-id')
    return render(request,'Assignment/index.html',{'assignment':assignment})

@login_required
def new(request):
    if(request.method == 'POST'):
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            point = user.profile.points
            if (point != 0):
                points = point -1
                user.profile.points = points
                user.profile.save()
                assignment = form.save(commit=False)
                assignment.created_user = request.user
                assignment.save()
                return redirect('Assignment:detail',assignment.pk)
            else:
                messages.info(request, '포인트가 없습니다.')
                return redirect('Assignment:index')
        return redirect('Assignment:index')
    else:
        form = AssignmentForm()
    return render(request,'Assignment/form.html',{'form':form})

def detail(request,pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignmentUsers = AssignmentUser.objects.filter(assignment=pk)
    checkAs = AssignmentUser.objects.filter(assignment=pk,user=request.user.pk)
    if (request.method == 'POST'):
        if(checkAs.exists()):
            messages.info(request, '이미 과제를 참여했습니다.')
            return redirect('Assignment:detail',assignment.pk)
        assignmentUser = AssignmentUser()
        assignmentUser.assignment = assignment
        assignmentUser.user = request.user
        assignmentUser.save()
        messages.info(request, '과제 참여완료')
        return redirect('Assignment:detail',assignment.pk)
    else:
        return render(request,'Assignment/detail.html',{
            'assignment':assignment,
            'count':assignmentUsers.count(),
            'checkAs': checkAs,
            'submissions': assignment.submission_set.all()
        })

@login_required
def submit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if (request.method == 'POST'):
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.writer = request.user
            submission.assignment = assignment
            submission.status = 'requested'
            submission.save()
            return redirect('Assignment:detail', assignment.pk)
        else:
            messages.info(request, '제출 실패')
            return redirect('Assignment:detail', assignment.pk)
    else:
        form = SubmissionForm()
    return render(request, 'Assignment/submit.html', {'form':form})