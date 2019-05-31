from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Submission, Coaching

def detail(request, pk):
    submission =  get_object_or_404(Submission, pk=pk)
    content = {
        'submission' : submission,
        'coachings' : submission.coaching_set.all()
    }
    return render(request, 'Submission/detail.html', content)

@login_required
def success(request, pk):
    submission =  get_object_or_404(Submission, pk=pk)
    user = request.user
    if request.method == 'POST':
        if user.id == submission.writer.id:
            profile = submission.writer.profile
            profile.points += 1
            submission.status = 'succeed'
            profile.save()
            submission.save()
    return redirect('Submission:detail', pk)

@login_required
def fail(request, pk):
    submission =  get_object_or_404(Submission, pk=pk)
    user = request.user
    if request.method == 'POST':
        if user.id == submission.writer.id:
            submission.status = 'failed'
            submission.save()
    return redirect('Submission:detail', pk)

@login_required
def create_coaching(request, submission_pk):
    submission = get_object_or_404(Submission, pk=submission_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        writer = request.user
        coaching = Coaching(content=content, submission=submission, writer=writer)
        coaching.save()
    return redirect('Submission:detail', submission_pk)
