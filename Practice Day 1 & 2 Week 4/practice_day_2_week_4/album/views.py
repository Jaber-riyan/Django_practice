from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import AlbumModel

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = AlbumForm()
        return render(request,'add_album.html',{'form':form})
    
    
def edit_album(request, id):
    post = AlbumModel.objects.get(pk=id)
    form = AlbumForm(instance=post)
    # print(post.name)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        
    return render(request,'add_album.html',{'form':form})

def delete_album(request,id):
    delete = AlbumModel.objects.get(pk=id)
    delete.delete()
    return redirect('homepage')