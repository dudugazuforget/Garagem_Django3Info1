from rest_framework.serializers import ModelSerializer;

from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        Model = Categoria
        fields = "__all__"
