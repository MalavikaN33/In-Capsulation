from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('handleSignup', views.handleSignup, name='handleSignup'),
    path('handleLogin', views.handleLogin, name='handleLogin'),
    path('handleLogout',views.handleLogout,name='handleLogout'),
]