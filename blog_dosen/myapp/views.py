from django.shortcuts import render
from .models import Publikasi

def publikasi_view(request):
    publikasi_list = Publikasi.objects.all()
    return render(request, 'myapp\publikasi.html', {'publikasi_list': publikasi_list})

def detail_project(request):
    return render(request, 'myapp\detailProject.html')

def landing_page(request):
    return render(request, 'myapp\landingpage.html')

def pkm_(request):
    return render(request, 'myapp\pkm.html')
