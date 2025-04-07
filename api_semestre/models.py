from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
# Create your models here.

@deconstructible
class RenameImage(object):
    def __init__(self,subdir='imagens'):
        self.subdir = subdir

    def __call__(self, instance, filename):
        extension = filename.split('.')[-1]
        new_name =f"{uuid.uuid4()}.{extension}"
        return os.path.join(self.subdir,new_name)
    
class CadastroFilme(models.Model):
    Nome = models.CharField (max_length=100)
    Imagem = models.ImageField(upload_to=RenameImage('imagens/'))
    NomeAutor = models.CharField(max_length=100)


@deconstructible
class RenameImage(object):
    def __init__(self,subdir='imagens'):
        self.subdir = subdir

    def __call__(self, instance, filename):
        extension = filename.split('.')[-1]
        new_name =f"{uuid.uuid4()}.{extension}"
        return os.path.join(self.subdir,new_name)

class CadastroPerfil(models.Model):
    Nome = models.CharField (max_length=100)
    Foto = models.ImageField(upload_to=RenameImage('imagens/'))
    Bio = models.CharField(max_length=300)

class CadastroResenha(models.Model):
    Comentário = models.CharField(max_length=1000)
    Filme = models.ForeignKey(CadastroFilme, on_delete=models.DO_NOTHING)
    Perfil = models.ForeignKey(CadastroPerfil, on_delete=models.DO_NOTHING)