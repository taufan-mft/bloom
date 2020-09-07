from django.urls import path

from . import views


urlpatterns = [
 path('', views.home),
 path('second/', views.secondpage),
 path('seblak-bloom/', views.viewSeblak),
 path('bloom-raw-honey/', views.viewMadu),
 path('franchise/', views.viewFranchise),
 path('daftar-outlet/', views.viewLokasiOutlet),
 path('tentang-kami/', views.viewTentang)
]