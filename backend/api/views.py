from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import random
from .pokemon_class import Pokemon

def home_view(request):
    context = {
        'page_title': 'Home Page - Pokemon Duel Simulator',
    }
    return render(request, 'home.html', context)

def about_view(request):
    context = {
        'page_title': 'About Page - Pokemon Duel Simulator',
    }
    return render(request, 'about.html', context)

def support_view(request):
    context = {
        'page_title': 'Support Page - Pokemon Duel Simulator',
    }
    return render(request, 'support.html', context)

def contact_view(request):
    context = {
        'page_title': 'Contact-Us Page - Pokemon Duel Simulator',
    }
    return render(request, 'contact.html', context)

class GenerateTeamView(View):
    def get(self, request):
        random_team = [Pokemon(id) for id in random.sample(range(1,1026), 6)]

        team_data = []

        for pokemon in random_team:
            pokemon_data = {
                'id' : pokemon.id,
                'name' : pokemon.name,
                'level' : pokemon.level,
                'types' : pokemon.types,
                'moves' : [move.name for move in pokemon.moves],
                'stats' : {
                    'hp' : pokemon.hp,
                    'attack' : pokemon.attack,
                    'defense' : pokemon.defense,
                    'special_attack' : pokemon.special_attack,
                    'special_defense' : pokemon.special_defense,
                    'speed' : pokemon.speed,
                },
                'nature' : pokemon.nature,
            }
            team_data.append(pokemon_data)

        return JsonResponse(team_data, safe=False)
