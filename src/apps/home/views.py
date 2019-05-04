from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render, redirect
from src.forms.auth.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from src.models.post.models import Post
from django.contrib.auth import authenticate, login


class HomeView(ListView):
    queryset      = Post.objects.all()
    template_name = 'home/home.html'



class RegisterView(View):
    template_name   = 'auth/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        else:
            form = RegisterForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['login'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home:login_page')
        else:
            return redirect('home:register_page')


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
