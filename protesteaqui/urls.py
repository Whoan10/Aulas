from django import views
from django.urls import URLPattern, path

from . import views

urlpatterns = {
    path('', views.home, name = 'home'),
    path('home/', views.teste, name = 'home'),
    path('ola/', views.ola, name = 'home' )
}