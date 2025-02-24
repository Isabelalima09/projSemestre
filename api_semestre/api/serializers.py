from rest_framework import serializers
from api_semestre import models

class CadastroFilmeSerializer(serializers.ModelSerializer):
      class meta:
            model = models.CadastroFilme
            fields="__all__"

class CadastroResenhaSerializer(serializers.ModelSerializer):
      class meta:
            model= models.CadastroResenha
            fields= "__all__"

class CadastroPerfilSeralizer(serializers.ModelSerializer):
      class meta:
            model = models.CadastroPerfil
            fields= "__all__"