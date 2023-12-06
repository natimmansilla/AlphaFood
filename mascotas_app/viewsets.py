from rest_framework.viewsets import ModelViewSet
from .models import Mascota
from .serializers import MascotaSerializer

class MascotaViewSet(ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer