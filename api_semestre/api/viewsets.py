from rest_framework import viewsets
from api_semestre.api import serializers
from api_semestre import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404 
from django.db.models import Count
class CadastroFilmeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroFilmeSerializer
    queryset = models.CadastroFilme.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastro de filme",
        responses={200: serializers.CadastroFilmeSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo cadastro de filme",
        responses={201: "Cadastro de filme realizado com sucesso!"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastro do filme conforme o ID informado",
        responses={200: "Cadastro de filme encontrado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastro do filme conforme ID e dados informados",
        responses={200: "Cadastro de filme alterado com sucesso!"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta cadastro de filme conforme ID e dados informado",
        responses={200: "Cadastro de filme deletado com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o total de resenhas por filme",
        responses={200: 'Total de resenhas por filme'}
    )
    @action(detail=False, methods=['get'])
    def ResenhaTotal_filme(self, request):
        resenhasTotal = models.CadastroFilme.objects.annotate(ResenhaTotal = Count('cadastroresenha__id')).values('Nome', 'ResenhaTotal')
        filTotSerializer = serializers.TotaldeCadastroFilmeSerializer(resenhasTotal, many=True)
        return Response(filTotSerializer.data)

class CadastroResenhaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroResenhaSerializer
    queryset = models.CadastroResenha.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastro de resenha",
        responses={200: serializers.CadastroResenhaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo cadastro de resenha",
        responses={201: "Cadastro de resenha realizado com sucesso!"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastro da renha conforme o ID informado",
        responses={200: "Cadastro da resenha encontrado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastro da resenha conforme ID e dados informados",
        responses={200: "Cadastro de resenha alterado com sucesso!"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta cadastro de resenha conforme ID e dados informado",
        responses={200: "Cadastro de resenha deletado com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CadastroPerfilViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroPerfilSerializer
    queryset = models.CadastroPerfil.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastro de perfil",
        responses={200: serializers.CadastroPerfilSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo cadastro de perfil",
        responses={201: "Cadastro de perfil realizado com sucesso!"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastro de perfil conforme o ID informado",
        responses={200: "Cadastro de perfil encontrado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastro de perfil conforme ID e dados informados",
        responses={200: "Cadastro de perfil alterado com sucesso!"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta cadastro de perfil conforme ID e dados informado",
        responses={200: "Cadastro de perfil deletado com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o total de resenhas por perfil",
        responses={200: 'Total de renhas por perfil'}
    )
    @action(detail=False, methods=['get'])
    def ResenhaTotal_perfil(self, request):
        resenhasTotal = models.CadastroPerfil.objects.annotate(ResenhaTotal = Count('cadastroresenha__id')).values('Nome', 'ResenhaTotal')
        perfTotSerializer = serializers.TotaldeCadastroPerfilSerializer(resenhasTotal, many=True)
        return Response(perfTotSerializer.data)