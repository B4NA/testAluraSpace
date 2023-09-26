from django.urls import path
from galeria.views import index, imagem, search

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photos_id>', imagem, name='imagem'),
    path('search', search, name='search')
]