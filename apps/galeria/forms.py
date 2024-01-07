from django import forms
from apps.galeria.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['publicada']
        labels = {
            'nome':'Nome da imagem',
            'legenda':'Legenda da imagem',
            'category':'Categoria',
            'image':'Arquivo da imagem',
            'description':'Descrição',
            'data':'Data de registro',
            'user':'Usuário',
        }

        widget = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'user': forms.Select(attrs={'class':'form-control'}),
        }