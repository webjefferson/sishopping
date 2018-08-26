from rest_framework.viewsets import ModelViewSet

from apps.contacontabil.models import ContaContabil
from apps.contacontabil.api.serializers import ContaContabilSerializer


class ContaContabilViewSet(ModelViewSet):
    queryset = ContaContabil.objects.all()
    serializer_class = ContaContabilSerializer
