from rest_framework import serializers
from api_semestre import models

class CadastroFilmeSerializer(serializers.ModelSerializer):
      class Meta:
            model = models.CadastroFilme
            fields="__all__"

class CadastroResenhaSerializer(serializers.ModelSerializer):
      class Meta:
            model= models.CadastroResenha
            fields= "__all__"

class CadastroPerfilSeralizer(serializers.ModelSerializer):
      class Meta:
            model = models.CadastroPerfil
            fields= "__all__"