from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    LoginView,
    RegisterView,
    NewView,
    DetailView,
    CreateView
)


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('create/', CreateView.as_view(), name='create_page'),
    path('article<int:pk>/', DetailView.as_view(), name='detail_page'),
    path('new/', NewView.as_view(), name='new_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('admin/', admin.site.urls),
]
