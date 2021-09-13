from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import EditProfileForms
@login_required(login_url='/')
def editProfile(request):
    if request.method=='POST':
       form = EditProfileForms(request.POST, request.FILES, instance=request.user)
       if form.is_valid():
           form.save()
           messages.success(request, 'Profile successfully updated')


    else:
        form = EditProfileForms(instance=request.user)
    return render(request, 'pages/edit_profile.html',context={'form':form})
