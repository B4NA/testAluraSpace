from django.contrib import admin
from apps.galeria.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome',)
    list_filter = ('category', 'user',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Photo, ListPhotos)
