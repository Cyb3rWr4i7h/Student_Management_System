from django.contrib import admin
from django.urls import path, include
from sms import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("help/", views.help, name="help"),
    path("signup/", views.signup, name="signup")
]
