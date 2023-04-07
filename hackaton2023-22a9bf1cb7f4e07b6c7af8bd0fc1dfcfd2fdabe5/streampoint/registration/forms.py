from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from lkusers.models import ContribUsers
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-quiz'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'name-quiz'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-quiz'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'name-quiz'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'name-quiz'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




