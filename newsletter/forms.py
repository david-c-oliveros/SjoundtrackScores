from django.forms import ModelForm
from .models import *


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title']


class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = '__all__'


class FirstImpressionsForm(ModelForm):
    class Meta:
        model = FirstImpressions
        fields = '__all__'


class NeverGetsOldForm(ModelForm):
    class Meta:
        model = NeverGetsOld
        fields = '__all__'


class ComposerSpotlightForm(ModelForm):
    class Meta:
        model = ComposerSpotlight
        fields = '__all__'
