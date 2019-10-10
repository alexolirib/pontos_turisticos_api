#view baseada em classe
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from ponto_turistico.api.serializers import PontoTuristicoSerializer
from ponto_turistico.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    #actions padrões
    #get geral /
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    #quando for post
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # delete /{valor obrigatório "Recurso" }
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # get /{valor obrigatório "Recurso" }
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    #put
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    #patch
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    #detail=True -> passa a PK
    # por conta do detail é preciso mandar o pk
    # logo fica  /pontoturistico/{pk}/denunciar
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    #fica só /pontoturistico/teste
    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        pass
