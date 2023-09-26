from django.contrib import admin
from galeria.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome',)
    list_filter = ('category',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Photo, ListPhotos)
