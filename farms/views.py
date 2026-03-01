from rest_framework import viewsets
from .models import Farm
from .serializers import FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()   # 👈 add this
    serializer_class = FarmSerializer

    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)