from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()   # ✅ ADD THIS
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)