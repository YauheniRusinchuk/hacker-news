from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    LoginView,
    RegisterView,
    NewView,
    DetailView,
    CreateView,
    UpdateView,
    DeletePost
)


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('article<int:pk>/update/', UpdateView.as_view(), name='update_page'),
    path('article<int:pk>/delete/', DeletePost.as_view(), name='delete_page'),
    path('article/create/', CreateView.as_view(), name='create_page'),
    path('article<int:pk>/', DetailView.as_view(), name='detail_page'),
    path('new/', NewView.as_view(), name='new_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('admin/', admin.site.urls),
]
