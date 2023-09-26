from django.shortcuts import render, get_object_or_404
from galeria.models import Photo

def index(request):
    Fotos = Photo.objects.order_by('data').filter(publicada=True)
    return render(request, 'AluraSPACE/index.html', {'cards': Fotos})

def imagem(request, photos_id):
    photo = get_object_or_404(Photo, pk=photos_id)
    return render(request, 'AluraSPACE/imagem.html', {'photos': photo})

def search(request):
    Fotos = Photo.objects.order_by('data').filter(publicada=True)

    if 'search' in request.GET: 
        GetPhoto = request.GET['search']
        if GetPhoto: Fotos = Photo.objects.filter(nome__icontains = GetPhoto)

    return render(request, 'AluraSPACE/search.html', {'cards': Fotos})