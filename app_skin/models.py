from django.db import models

class Skin(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='skins/covers/%Y/%m/%d/', default='', blank=True)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    