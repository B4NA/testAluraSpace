from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Photo(models.Model):
    optionsCategory = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
        ('SATÉLITE', 'Satélite')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=optionsCategory, default='')
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __str__(self):
        return str(self.nome)
