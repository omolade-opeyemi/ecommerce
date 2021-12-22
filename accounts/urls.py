from . import views
from django.urls import path

urlpatterns = [
    path('login.html', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('register.html', views.registerPage, name='register'), 
    path('forgetpass.html', views.forgetpassPage, name='forgetpass'),

] 