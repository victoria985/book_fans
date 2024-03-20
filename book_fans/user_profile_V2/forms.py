from django import forms
from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileV2
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Pakeičiame į get_user_model su skliaustais
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileV2
        fields = ['picture']

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Pakeičiame į get_user_model su skliaustais
        fields = ("first_name", "last_name", "email", )
