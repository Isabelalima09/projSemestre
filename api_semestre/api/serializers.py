from rest_framework import serializers
from api_semestre import models



class CadastroFilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CadastroFilme
        fields = "__all__"
        extra_kwargs={
            'id': {'help_text': 'Indicador do cadastro de filme'},
            'Nome': {'help_text': 'Nome do autor do filme cadastrado'},
            'Imagem': {'help_text': 'Imagem representando a capa do filme'},
            'NomeAutor': {'help_text': 'Nome do autor do filme cadaastrado'},
        }

class TotaldeCadastroFilmeSerializer(serializers.Serializer):
    Nome = serializers.CharField()
    ResenhaTotal = serializers.DecimalField(max_digits=10, decimal_places=2)

class CadastroResenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CadastroResenha
        fields = "__all__"
        extra_kwargs={
            'id': {'help_text': 'Indicador do cadastro de resenha'},
            'Comentário': {'help_text': 'Resenha - opinião sobre o filme'},
        }

class CadastroPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CadastroPerfil
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Indicador do cadastro de perfil'},
            'Nome':{'help_text': 'Nome do usuário'},
            'Foto':{'help_text': 'Foto de perfil do usuário'},
            'Bio':{'help_text': 'Biografia com informações da preferência do suário'},
        }

class TotaldeCadastroPerfilSerializer(serializers.Serializer):
    Nome = serializers.CharField()
    ResenhaTotal = serializers.DecimalField(max_digits=10, decimal_places=2)