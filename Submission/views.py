from django.shortcuts import render
from django.http import HttpResponse

from .models import Submission

def detail(request, pk):
    submission = Submission.objects.get(pk=pk)
    return render(request, 'Submission/detail.html', {'submission' : submission})