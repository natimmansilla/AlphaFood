from rest_framework.serializers import ModelSerializer
from .models import Mascota

class MascotaSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = "__all__"