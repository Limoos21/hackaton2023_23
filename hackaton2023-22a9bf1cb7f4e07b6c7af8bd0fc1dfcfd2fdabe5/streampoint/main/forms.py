from django import forms
from lkusers.models import ContribUsers, History


class ContribUserForm(forms.ModelForm):
    class Meta:
        model = ContribUsers
        fields = []


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = []
