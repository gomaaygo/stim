from rest_framework import serializers

from .models import Person, AQChild
      

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
        read_only_fields = ['class_asd']  

class AQChildSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = AQChild
        fields = ['a1_score', 'a2_score', 'a3_score', 'a4_score', 'a5_score',
                   'a6_score', 'a7_score', 'a8_score', 'a9_score', 'a10_score',
                   'result', 'person']
        read_only_fields = ['result']
        
    def create(self, validated_data):
        person = Person.objects.create(**validated_data.pop('person'))
        obj = AQChild.objects.create(person=person, **validated_data)
        
        return obj