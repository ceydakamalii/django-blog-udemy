from django import forms
from django.db.models import fields
from blog.models import ContactModel
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
       model = ContactModel
       fields = ('email','first_name','last_name','message')

    def send_email(self,message):
        send_mail(
            subject='There is a new message from the contact form',
            message=message,
            recipient_list=['ceydakamali3@gmail.com'],
            fail_silently=False
        )



""" class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea) """

