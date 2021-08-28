from django.shortcuts import redirect, HttpResponse
from courses import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import ValidationError


class loginf(AuthenticationForm):
    username = forms.EmailField(required=True, label='email', widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("error message 1")
        except:
            try:
                user_login = authenticate(
                    username=user.username, password=password)
            except:
                user_login = None
            if user_login is not None:
                return user_login
            else:
                raise forms.ValidationError("error message 1")
