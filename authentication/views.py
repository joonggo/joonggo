from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm as LoginForm
# Create your views here.

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
    else:
        form=SignupForm()
    return render(request,'accounts/signup_form.html',{
                'form':form,
                })

