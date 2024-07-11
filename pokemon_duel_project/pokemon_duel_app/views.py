from django.shortcuts import render
from rest_framework import generics
from .serializers import PokemonSerializer
from .models import Pokemon

# Create your views here.

def index(request):
    return render(request, 'index.html')

class PokemonView(generics.ListAPIView): #A view that is set up to return all of the different pokemon
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer