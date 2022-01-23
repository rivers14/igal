from django.shortcuts import render
from imggal.models import imgggal

def imgdisplay(request):
    resultsdisplay=imgggal.objects.all()
    return render(request,'index.html',{'imgggal':resultsdisplay})
