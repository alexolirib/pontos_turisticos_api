from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#essa é a forma de registrar as rotas do rest api
from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from enderecos.api.viewsets import EnderecoViewSet
from ponto_turistico.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
#router.register(nome da rota, viewset)
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
