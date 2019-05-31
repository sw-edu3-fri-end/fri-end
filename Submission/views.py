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
        if user.id == submission.assignment.created_user.id:
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
        if user.id == submission.assignment.created_user.id:
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

@login_required
def like_coaching(request, submission_pk, coaching_pk):
    coaching = get_object_or_404(Coaching, pk=coaching_pk)
    user = request.user
    if coaching.like_users.filter(pk=user.pk).exists():
        coaching.like_users.remove(user)
    else:
        coaching.like_users.add(user)
    return redirect('Submission:detail', submission_pk)