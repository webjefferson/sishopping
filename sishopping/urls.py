"""sishopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from apps.banco.api.viewset import BancoViewSet
from apps.empresa.api.viewset import EmpresaViewSet
from apps.setor.api.viewset import SetorViewSet
from apps.colaborador.api.viewset import ColaboradorViewSet
from apps.centrocusto.api.viewset import CentroCustoViewSet
from apps.contacontabil.api.viewset import ContaContabilViewSet
from apps.rateio.api.viewset import RateioViewSet
from apps.orcamento.api.viewset import OrcamentoViewSet
from apps.endereco.api.viewset import EnderecoViewSet
from apps.retencoes.api.viewset import RetencoesViewSet
from apps.fornecedor.api.viewset import FornecedorViewSet
from apps.rp.api.viewset import RpViewSet

router = routers.DefaultRouter()
router.register('bancos', BancoViewSet)
router.register('empresas', EmpresaViewSet)
router.register('setores', SetorViewSet)
router.register('colaboradores', ColaboradorViewSet)
router.register('centroscustos', CentroCustoViewSet)
router.register('contascontabeis', ContaContabilViewSet)
router.register('rateios', RateioViewSet)
router.register('orcamentos', OrcamentoViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('retencoes', RetencoesViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('rps', RpViewSet)

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
