from rest_framework import serializers
from .models import Pessoa, Endereco


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('url', 'nome', 'idade')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('url', 'cidade', 'logradouro','numero', 'complemento', 'pessoa')
