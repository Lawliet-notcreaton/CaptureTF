from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm, TextInput, Textarea

class TicketsForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['topic','message']
        widgets = {
            'topic' : TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Тема'
                }),

            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Cooбщение'
            }),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
