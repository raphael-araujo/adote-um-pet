from django.db import models

# Create your models here.


class Pet(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    historia = models.TextField(blank=False, null=False)
    foto = models.URLField(blank=False, null=False)