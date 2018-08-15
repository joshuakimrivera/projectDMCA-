from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

from . import views


app_name = "account"

urlpatterns = [
    path('account/', views.dashboard, name='dashboard'),
]
