from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from src.forms.auth.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class HomeView(TemplateView):
    template_name = 'home/home.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        else:
            form = LoginForm()
            return render(request, 'auth/login.html', {"form" : form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')
            else:
                return redirect('home:login_page')
