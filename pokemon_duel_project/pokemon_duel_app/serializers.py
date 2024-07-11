from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'level', 'types', 'moves', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed', 'nature',)