import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import News


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', max_length=255,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', max_length=255,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Колдонуучу аты:', max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput(attrs={'class': 'form-control'})
    username = forms.CharField(label='Колдонуучу аты:', max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['category', 'title', 'content', 'is_published', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры.')
        return title
