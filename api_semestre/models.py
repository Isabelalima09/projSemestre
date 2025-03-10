from django.db import models

class CadastroFilme(models.Model):
    Nome = models.CharField(max_length=20)
    imagem= models.ImageField()
    NomeAutor= models.CharField(max_length=30)

class CadastroResenha(models.Model):
    Comentario=models.CharField(max_length=1000)

class CadastroPerfil(models.Model):
    Nome=models.CharField(max_length=20)
    Foto=models.ImageField()
    Bio=models.CharField(max_length=50)