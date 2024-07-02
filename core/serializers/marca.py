from rest_framework.serializers import ModelSerializer

from core.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        Model = Marca
        fields = "__all__"
