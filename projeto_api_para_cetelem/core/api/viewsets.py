from rest_framework.viewsets import ModelViewSet
from core.models import CompoundName
from .serializers import CompoundNameSerializer


class CompoundNameViewSet(ModelViewSet):
    queryset = CompoundName.objects.all()
    serializer_class = CompoundNameSerializer
