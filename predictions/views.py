from rest_framework.viewsets import ModelViewSet
from .models import PredictionRecord
from .serializers import PredictionSerializer


class PredictionViewSet(ModelViewSet):
    queryset = PredictionRecord.objects.all()
    serializer_class = PredictionSerializer