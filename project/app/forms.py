from django import forms
from django.contrib.auth.models import User


class UserRegistration(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter User name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter email'}))
    password1 = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2 = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter confirm password'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")