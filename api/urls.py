from django.contrib import admin
from django.urls import include, path
from api.views import PessoaView, EnderecoView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoaView)
router.register('enderecos', EnderecoView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('pessoaupdate/<int:id>', views.pessoaUpdate),

]
