from django .contrib.auth.forms import UserChangeForm
from django.forms.models import fields_for_model
from account.models import CustomUserModel

class EditProfileForms(UserChangeForm):
    password = None
    class Meta:
        model = CustomUserModel
        fields = ('email','first_name','last_name','avatar')