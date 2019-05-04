from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    login       = forms.CharField(label='Логин')
    password    = forms.CharField(label='Пароль', widget=forms.PasswordInput)



class RegisterForm(forms.Form):
    login       = forms.CharField(label='Логин')
    password    = forms.CharField(label='Пароль', widget=forms.PasswordInput)


    def clean_login(self):
        username = self.cleaned_data.get('login')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return username
