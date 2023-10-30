from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Photo
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

    Fotos = Photo.objects.order_by('data').filter(publicada=True)
    return render(request, 'AluraSPACE/index.html', {'cards': Fotos})

def imagem(request, photos_id):
    photo = get_object_or_404(Photo, pk=photos_id)
    return render(request, 'AluraSPACE/imagem.html', {'photos': photo})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    Fotos = Photo.objects.order_by('data').filter(publicada=True)

    if 'search' in request.GET: 
        GetPhoto = request.GET['search']
        if GetPhoto: Fotos = Photo.objects.filter(nome__icontains = GetPhoto)

    return render(request, 'AluraSPACE/search.html', {'cards': Fotos})

def startup(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    return render(request, 'AluraSPACE/startup.html')