from django.shortcuts import render

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
    return render(request, 'lokasi_outlet.html')


def viewTentang(request):
    return render(request, 'tentang-kami.html')