from django.shortcuts import render,redirect,get_object_or_404
from .forms import AssignmentForm
# Create your views here.
def index(request):
    return render(request,'Assignment/index.html')

def new(request):
    if(request.method == 'POST'):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.created_user = request.user
            assignment.save()
            return redirect('boards:detail',assignment.pk)
    else:
        form = AssignmentForm()
    return render(request,'Assignment/form.html',{'form':form})