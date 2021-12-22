from . import views
from django.urls import path

urlpatterns = [
    path('', views.contactPage, name='contact'),
]