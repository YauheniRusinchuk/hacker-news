from django.contrib import admin
from django.urls import path
from .views import HomeView, LoginView


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('admin/', admin.site.urls),
]
