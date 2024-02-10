from rest_framework import serializers
from .models import Dota2Teams, Dota2Players, Person

class Dota2TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dota2Teams
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'