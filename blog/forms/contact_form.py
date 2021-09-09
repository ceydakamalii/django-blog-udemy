from django import forms
from django.db.models import fields
from blog.models import ContactModel
class ContactForm(forms.ModelForm):
   class Meta:
       model = ContactModel
       fields = ('email','first_name','last_name','message')


""" class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea) """

