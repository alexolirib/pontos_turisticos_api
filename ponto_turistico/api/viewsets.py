#view baseada em classe
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ponto_turistico.api.serializers import PontoTuristicoSerializer
from ponto_turistico.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    #obriga está autenticado
    #DjangoModelPermissions --  ser baseada  as permissões do django admin
    permission_classes = (IsAuthenticated,) # para usuários admin é IsAdminUser
    # informa como o viewSet faz autenticação
    authentication_classes = (TokenAuthentication,)
    #buscar ?search={}
    filter_backends = (SearchFilter,)
    #endereco__linha1 = é possível buscar os objetos que se relaciona com o endereço pela a linha1
    search_fields = ('nome', 'descricao', 'endereco__linha1')

    #tem que ser campo único /1, poderia mudar 
    lookup_field = 'id'

    def get_queryset(self):
        # queryString /?id=1&nome=alexandre&descricao=hoje
        #se não passar o parametro irá padrão None
        id =self.request.query_params.get('id', None)
        nome =self.request.query_params.get('nome', None)
        descricao =self.request.query_params.get('descricao', None)
        #como é lazy load só irá buscar no final os objetos no banco
        #estou "pegando tudo e depois vou filtrando
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            #__iexact não importa o maiusculo ou o minusculo
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        return queryset

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
