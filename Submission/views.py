from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Submission

def detail(request, pk):
    submission =  get_object_or_404(Submission, pk=pk)
    return render(request, 'Submission/detail.html', {'submission' : submission})

def success(request, pk):
    # TODO : 해당 로직 실행자가 해당 과제 등록자인지 확인하는 로직 필요
    submission =  get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        # TODO : 해당 제출자의 point up 로직 필요
        submission.status = 'succeed'
        submission.save()
    return redirect('Submission:detail pk')

def fail(request, pk):
    # TODO : 해당 로직 실행자가 해당 과제 등록자인지 확인하는 로직 필요
    submission =  get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        submission.status = 'failed'
        submission.save()
    return redirect('Submission:detail pk')
