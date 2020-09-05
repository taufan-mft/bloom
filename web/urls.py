from django.urls import path

from . import views


urlpatterns = [
 path('', views.home),
 path('second/', views.secondpage),
 path('seblak-bloom/', views.viewSeblak),
]