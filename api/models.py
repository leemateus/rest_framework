from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(blank=True, max_length=100, null=True)
    pessoa = models.ManyToManyField(Pessoa)
