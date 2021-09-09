from django.shortcuts import render, redirect
from blog.forms import ContactForm
from blog.models import ContactModel

def contact(request):
  form = ContactForm()
  if request.method == 'POST':
   form = ContactForm(request.POST)
   if form.is_valid():
     """
     contact = ContactModel()
     contact.email = form.cleaned_data.get('email')
     contact.first_name = form.cleaned_data.get('first_name')
     contact.last_name = form.cleaned_data.get('last_name')
     contact.message = form.cleaned_data.get('message')
     contact.save()
     """
     form.save()
     return redirect('home')
  context={
      'form':form
  }
  return render(request, 'pages/contact.html', context=context)