from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Photo
from apps.galeria.forms import PhotoForm
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

    return render(request, 'AluraSPACE/index.html', {'cards': Fotos})

def adicionar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    form = PhotoForm

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia registrada.')

    return render(request, 'AluraSPACE/adicionar.html', {'form' : form})

def editar(request, photos_id, delete=False):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    photo = Photo.objects.get(id=photos_id)

    if delete == True:
        photo.delete()
        messages.success(request, 'Fotografia deletada com sucesso.')
        return redirect('index')
    else:
        form = PhotoForm(instance=photo)
        
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES, instance=photo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Fotografia editada com sucesso.')

        return render(request, 'AluraSPACE/editar.html', {'form' : form, 'photos_id' : photos_id, 'delete' : delete})
    
def filtro(request, category):
    photo = Photo.objects.order_by('data').filter(publicada=True, category=category)
    return render(request, 'AluraSPACE/index.html', {'cards' : photo})