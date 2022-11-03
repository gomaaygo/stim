from rest_framework import serializers

from .models import Person, AQChild


class AQChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = AQChild
        fields = ('__all__')
        

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')