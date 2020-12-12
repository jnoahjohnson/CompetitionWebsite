from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This page extends the default creation form to get more information for our model


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    first_name = forms.CharField(
        max_length=30, required=False)
    last_name = forms.CharField(
        max_length=30, required=False)
    email = forms.EmailField(
        max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
