from rest_framework.viewsets import ModelViewSet

from apps.setor.models import Setor
from apps.setor.api.serializers import SetorSerializer


class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
