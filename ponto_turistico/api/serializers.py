from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco
from ponto_turistico.models import PontoTuristico, DocIdentificador


class DocIdentificadorSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificador
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    #é preciso botar read_only -> por conta não se obrigado quando for feito o post (assim vai ignorar esse campo memso se mandar
    # atracoes = AtracaoSerializer(many=True, read_only=True)
    #relacionamento manyToMany
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificador = DocIdentificadorSerializer()

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
                  'doc_identificador',
                  'descricao_completa',
                  'descricao_completa2'
        )
        read_only_fields =('comentarios', 'avaliacoes')

    def criar_doc_identificador(self, documento, ponto_turistico):
        doc = DocIdentificador.objects.create(**documento)
        ponto_turistico.doc_identificador = doc


    def criar_atracoes(self, atracoes, ponto_turistico):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto_turistico.atracoes.add(at)

    def criar_endereco(self, endereco, ponto_turistico):
        end = Endereco.objects.create(**endereco)
        ponto_turistico.endereco = end


    #para criar a variável que se relaciona
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        #deletando
        del validated_data['atracoes']
        endereco = validated_data['endereco']
        del validated_data['endereco']

        documento = validated_data['doc_identificador']
        del validated_data['doc_identificador']



        ponto_turistico = PontoTuristico.objects.create(**validated_data)
        self.criar_atracoes(atracoes, ponto_turistico)
        self.criar_endereco(endereco, ponto_turistico)
        self.criar_doc_identificador(documento, ponto_turistico)

        ponto_turistico.save()



        return ponto_turistico

    def get_descricao_completa(self, obj):
        #pode pegar atributos do objeto que nem estão sendo usado
        #nos fields
        return '%s - %s' % (obj.nome, obj.descricao)
