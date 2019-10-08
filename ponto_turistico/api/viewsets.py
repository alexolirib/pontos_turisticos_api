#view baseada em classe
from rest_framework.viewsets import ModelViewSet

from ponto_turistico.api.serializers import PontoTuristicoSerializer
from ponto_turistico.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
