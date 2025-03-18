from rest_framework import viewsets
from api_semestre.api import serializers 
from api_semestre import models 
from drf_yasg.utils import swagger_auto_schema

class CadastroFilmeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroFilmeSerializer
    queryset = models.CadastroFilme.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastrar todos os filmes",
        response={200:serializers.CadastroFilmeSerializer(many=True)}
    )
    def list(self,request,*args,**kwargs):
        return super().list(request,*args,**kwargs)
    @swagger_auto_schema(
        operation_description="Cria um nova cadastroFilme",
        responses={201: "CadastroFilme criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        #metodo POST
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastroFilme conforme o ID informado",
        responses={200: "CadastroFilme encontrada"}
    )
    def retrieve(self, request, *args, **kwargs):
        #metodo GET com ID
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastroFilme conforme ID e dados informados",
        responses={200: "CadastroFilme alterada com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        # metodo PUT
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o cadastroFilme conforme ID informado",
        responses={204: "CadastroFilme deletado com sucesso"}
  )
    def destroy(self, request, *args, **kwargs):
        #metdodo delete
        return super().update(request,*args,**kwargs)

class CadastroResenhaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroResenhaSerializer
    queryset = models.CadastroResenha.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastrar todas as resenhas",
        response={200:serializers.CadastroFilmeSerializer(many=True)}
    )
    def list(self,request,*args,**kwargs):
        return super().list(request,*args,**kwargs)
    @swagger_auto_schema(
        operation_description="Cria um novo cadastroResenha",
        responses={201: "CadastroResenha criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        #metodo POST
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastroResenha conforme o ID informado",
        responses={200: "CadastroResenha encontrada"}
    )
    def retrieve(self, request, *args, **kwargs):
        #metodo GET com ID
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastroResenha conforme ID e dados informados",
        responses={200: "CadastroResenha alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        # metodo PUT
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o cadastroResenha conforme ID informado",
        responses={204: "CadastroResenha deletado com sucesso"}
  )
    def destroy(self, request, *args, **kwargs):
        #metdodo delete
        return super().update(request,*args,**kwargs)


class CadastroPerfilViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroPerfilSeralizer
    queryset = models.CadastroFilme.objects.all()
    @swagger_auto_schema(
        operation_description="Cadastrar o perfil",
        response={200:serializers.CadastroFilmeSerializer(many=True)}
    )
    def list(self,request,*args,**kwargs):
        return super().list(request,*args,**kwargs)
    @swagger_auto_schema(
        operation_description="Cria um novo cadastroPerfil",
        responses={201: "CadastroFilme criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        #metodo POST
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o cadastroPerfil conforme o ID informado",
        responses={200: "CadastroPerfil encontrada"}
    )
    def retrieve(self, request, *args, **kwargs):
        #metodo GET com ID
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cadastroPerfil conforme ID e dados informados",
        responses={200: "CadastroPerfil alterada com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        # metodo PUT
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o cadastroPerfil conforme ID informado",
        responses={204: "CadastroPerfil deletado com sucesso"}
  )
    def destroy(self, request, *args, **kwargs):
        #metdodo delete
        return super().update(request,*args,**kwargs)
