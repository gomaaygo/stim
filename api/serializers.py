from dataclasses import fields
from rest_framework import serializers

from .models import Person, AQChild


class AQChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = AQChild
        fields = ('__all__')