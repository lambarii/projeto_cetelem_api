from rest_framework.serializers import ModelSerializer
from core.models import CompoundName


class CompoundNameSerializer(ModelSerializer):
    class Meta:
        model = CompoundName
        fields = ['id', 'nome_Completo']
