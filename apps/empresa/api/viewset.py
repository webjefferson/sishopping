from rest_framework.viewsets import ModelViewSet

from apps.empresa.models import Empresa
from apps.empresa.api.serializers import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
