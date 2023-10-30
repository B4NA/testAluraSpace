from django.db import models
from datetime import datetime

class UserAccount(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return str(self.nome)