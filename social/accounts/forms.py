from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CreateAccountForm(UserCreationForm):

    class Meta:
        fields=['username','email','password1','password2']
        model= get_user_model()

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['email'].label= 'Email Address'
        self.fields['password2'].label='Confirm Password'
        