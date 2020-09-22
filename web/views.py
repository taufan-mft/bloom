from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def secondpage(request):
    return render(request, 'inner-page.html')    


def viewSeblak(request):
    return render(request, 'seblak.html')


def viewMadu(request):
    return render(request, 'madu.html')


def viewFranchise(request):
    return render(request, 'inner-page.html')


def viewLokasiOutlet(request):
    kota = Kota.objects.all()
    dict = {
        'kotas':kota
    }
    return render(request, 'lokasi_outlet.html', dict)


def viewTentang(request):
    return render(request, 'tentang-kami.html')