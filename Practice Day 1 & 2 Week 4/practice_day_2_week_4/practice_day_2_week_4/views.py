from django.shortcuts import render,redirect
from album.models import AlbumModel



def home(request):
    data = AlbumModel.objects.all()
    print(data)
    return render(request, 'home.html' ,{'data':data})