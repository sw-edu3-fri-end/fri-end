from django.shortcuts import render,redirect,get_object_or_404
from .models import Assignment
from .forms import AssignmentForm


# Create your views here.
def index(request):
    assignment = Assignment.objects.all().order_by('-id')
    return render(request,'Assignment/index.html',{'assignment':assignment})

def new(request):
    if(request.method == 'POST'):
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.created_user = request.user
            assignment.save()
            return redirect('Assignment:index')
    else:
        form = AssignmentForm()
    return render(request,'Assignment/form.html',{'form':form})

def detail(request,pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignmentUsers = AssignmentUser.objects.filter(assignment=pk)
    if (request.method == 'POST'):
        checkAs = AssignmentUser.objects.filter(assignment=pk,user=request.user.pk)
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
        return render(request,'Assignment/detail.html',{'assignment':assignment,'count':assignmentUsers.count()})