from rest_framework import serializers
from api_semestre import models

class CadastroFilmeSerializer(serializers.ModelSerializer):
      class Meta:
            model = models.CadastroFilme
            fields="__all__"
            extra_kwargs={
                  'id':{'help_text':'Identificador do Filme'},
                  'Nome':{'help_text':'Nome do Filme'},
                  'Imagem':{'help_text':'Imagem do filme'},
                  'NomeAutor':{'help_text':'Nome do autor'}
            }

class CadastroResenhaSerializer(serializers.ModelSerializer):
      class Meta:
            model= models.CadastroResenha
            fields= "__all__"
            extra_kwrgs={
                  'id':{'help_text':'Identificador de resenha'},
                  'Comentario':{'help_text':'Opinião sobre o filme'}
            }

class CadastroPerfilSeralizer(serializers.ModelSerializer):
      class Meta:
            model = models.CadastroPerfil
            fields= "__all__"
            extra_kwargs={
                  'id':{'help_text':'Identificador do perfil'},
                  'Nome':{'help_text':'Nome do usuário'},
                  'Foto':{'help_text':'Foto do usuário no perfil'},
                  'Bio':{'help_text':'Descrição sobre o usuário'}
            }