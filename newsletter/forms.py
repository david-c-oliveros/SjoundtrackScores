from django.forms import ModelForm
from .models import *


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'


class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = ['content']
