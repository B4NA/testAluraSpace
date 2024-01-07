from django.urls import path
from apps.galeria.views import index, imagem, search, adicionar, editar, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photos_id>', imagem, name='imagem'),
    path('search', search, name='search'),
    path('adicionar', adicionar, name='adicionar'),
    path('editar/<int:photos_id>?delete=<int:delete>', editar, name='editar'),
    path('flt/<str:category>', filtro, name='filtro'),
]