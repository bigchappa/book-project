from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from . import models

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = get_user_model()
        fields = ('email', 'username')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['avatar', 'bio']