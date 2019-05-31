from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Submission, Coaching

def detail(request, pk):
    submission =  get_object_or_404(Submission, pk=pk)
    content = {
        'submission' : submission,
        'coachings' : submission.coaching_set.all()
    }
    return render(request, 'Submission/detail.html', content)

def success(request, pk):
    # TODO : 해당 로직 실행자가 해당 과제 등록자인지 확인하는 로직 필요
    submission =  get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        # TODO : 해당 제출자의 point up 로직 필요
        submission.status = 'succeed'
        submission.save()
    return redirect('Submission:detail', pk)

def fail(request, pk):
    # TODO : 해당 로직 실행자가 해당 과제 등록자인지 확인하는 로직 필요
    submission =  get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        submission.status = 'failed'
        submission.save()
    return redirect('Submission:detail', pk)

def create_coaching(request, submission_pk):
    submission = get_object_or_404(Submission, pk=submission_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        coaching = Coaching(content=content, submission=submission)
        coaching.save()
    return redirect('Submission:detail', submission_pk)
