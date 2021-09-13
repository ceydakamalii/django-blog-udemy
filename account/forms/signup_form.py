from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel

class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields = ('username','first_name','last_name','password1','password2')