from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from ponto_turistico.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id',
                  'nome',
                  'descricao',
                  'aprovado',
                  'foto',
                  'atracoes',
                  'comentarios',
                  'avaliacoes',
                  'endereco',
                  'descricao_completa',
                  'descricao_completa2'
        )

    def get_descricao_completa(self, obj):
        #pode pegar atributos do objeto que nem estão sendo usado
        #nos fields
        return '%s - %s' % (obj.nome, obj.descricao)
