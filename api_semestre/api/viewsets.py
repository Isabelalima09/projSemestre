from rest_framework import viewsets
from api_semestre.api import serializers 
from api_semestre import models 

class CadastroFilmeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroFilmeSerializer
    queryset = models.CadastroFilme.objects.all()

class CadastroResenhaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroResenhaSerializer
    queryset = models.CadastroResenha.objects.all()

class CadastroPerfilViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroPerfilSeralizer
    queryset = models.CadastroFilme.objects.all()