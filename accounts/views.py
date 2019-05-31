from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserCustomChangeForm
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect("Assignment:index")
        
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        
        
        if form.is_valid():
            user = form.save()
            
            profile = Profile(user=user.first_name)
            profile.save()
            auth_login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            return redirect('Assignment:index')
    else :
        form = UserCreationForm()
    return render(request,'accounts/auth_form.html',{'form':form})

def login(request):
    
    if request.user.is_authenticated:
        return redirect("Assignment:index")
        
    if request.method == "POST":
        form = AuthenticationForm(request , request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('Assignment:index')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('Assignment:index')
    return redirect('Assignment:index')
    
def delete(request):
    if request.method=='POST':
        request.user.delete()
    return redirect('Assignment:index')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST,instance = request.user)
        if form.is_valid:
            form.save()
            return redirect('Assignment:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    return render(request,'accounts/auth_form.html',{'form':form})
    
def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('AssertionError:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'accounts/auth_form.html',{'form':form})
    