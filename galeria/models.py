from django.db import models
from datetime import datetime

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

    def __str__(self):
        return str(self.nome)
