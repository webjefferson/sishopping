from rest_framework.serializers import ModelSerializer

from apps.fornecedor.models import Fornecedor, Telefone


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ('id', 'codigo_jde', 'cnpj', 'razao_social', 'nome_fantasia', 'insc_estad', 'insc_mun',
                  'data_situacao_cadastral', 'cnae', 'optante_simples', 'descricao_servicos_prestados',
                  'contato_empresa', 'telefone', 'banco', 'endereco',)


class TelefoneSerializer(ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('id', 'ddd', 'numero',)
