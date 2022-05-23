from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import views, login as auth_login
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
    return render(request,'signup.html',{'form':form})