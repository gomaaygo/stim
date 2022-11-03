from .serializers import AQChildSerializer, PersonSerializer

from .models import AQChild, Person

from rest_framework import viewsets


class AQChildViewSet(viewsets.ModelViewSet):
    serializer_class = AQChildSerializer
    queryset = AQChild.objects.all()
    

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
