from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'


class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = ['text', 'image', 'link_name', 'link_url']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
