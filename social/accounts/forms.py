from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Min
from .models import Account
from django.utils import timezone
class CreateAccountForm(UserCreationForm):

    class Meta:
        fields=['username','email','password1','password2']
        model= get_user_model()

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['email'].label= 'Email Address'
        self.fields['password2'].label='Confirm Password'
class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Account
        fields=['first_Name','last_Name','address','about','birth']
        allowed_age=18
        widgets={
            'birth':forms.SelectDateWidget(years=range(1930, timezone.now().year-allowed_age))

        }
