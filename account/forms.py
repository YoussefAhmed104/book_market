from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','email','last_name']

    def clean_paassword(self):
        cd = self.cleaned_data

        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("passwods don't match")
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','last_name']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','username','email','birth_data','photo']