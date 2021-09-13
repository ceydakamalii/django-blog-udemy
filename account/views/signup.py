from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import SignUpForm
from django.contrib.auth import login,authenticate

def signup(request):
    if request.method=='POST':
      form= SignUpForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password=password)
          login(request, user)
          return redirect('home')
    else:
        form= SignUpForm()
    return render(request, 'pages/signup.html',context={'form':form})
