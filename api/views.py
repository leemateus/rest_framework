from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Pessoa, Endereco
from .serializers import PessoaSerializer, EnderecoSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class PessoaView(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class EnderecoView(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

# @api_view(['PUT', 'GET', 'DELETE'])
@csrf_exempt
def pessoaUpdate(request, id):
    try:
        queryset = Pessoa.objects.get(id = id)
    except e:
        return Response(status = status.HTTP_404_NOT_DOUND)

    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = PessoaSerializer(queryset, data = data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
