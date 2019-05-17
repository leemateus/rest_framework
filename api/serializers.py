from rest_framework import serializers
from .models import Pessoa, Endereco

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'url', 'nome', 'idade')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'url', 'logradouro','numero', 'complemento', 'pessoa')
