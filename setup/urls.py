from django.contrib import admin
from django.urls import path,include
from api_semestre.api import viewsets
from rest_framework import routers,permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Proj_Semestre.API",#titulo = nome sistema
        default_version='v1', #versão a API
        description="Sistema para resenhas de filmes",#descrição do sistema
        terms_of_service="https://www.google.com/police/terms/", #se tiver um termo colocar um link
        contact=openapi.Contact(email="contato@resenha.com.br"), #email para contato
        license=openapi.License(name="Free"),#licensa

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
route=routers.DefaultRouter()
route.register(r'CadastroFilmes', viewsets.CadastroFilmeViewset, basename="Cadastro Filmes")
route.register(r'CadastroResenha', viewsets.CadastroResenhaViewset, basename="Cadastro Resenha")
route.register(r'CadastroPerfil', viewsets.CadastroPerfilViewset, basename="Cadastro Perfil")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
]

urlpatterns += [
    path('swaggerjson/', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
]
