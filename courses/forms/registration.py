from django.db.models.base import Model
from courses import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import ValidationError


class Register(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1    =   forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2    =   forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    def clean_email(self):
        usr_email = self.cleaned_data['email']
        usr = None
        try:
            usr = User.objects.get(email=usr_email)
        except:
            return usr_email
        if usr is not None:
            raise forms.ValidationError('email alredy exsist')
        else:
            print('new email')

