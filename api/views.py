from .serializers import AQChildSerializer

from .models import AQChild

from rest_framework import viewsets


class AQChildViewSet(viewsets.ModelViewSet):
    serializer_class = AQChildSerializer
    queryset = AQChild.objects.all()
