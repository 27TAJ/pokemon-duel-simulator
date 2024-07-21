from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
import random
from .pokemon_class import Pokemon
from.forms import Support_Ticket_Form

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

def support_view(request):
    if request.method == 'POST':
        form = Support_Ticket_Form(request.POST)
        if form.is_valid():
            form.save()
            form = Support_Ticket_Form()
            success_message = "Support Ticket submitted successfully. Thank you."
        else:
            success_message = None
    else:
        form = Support_Ticket_Form()
        success_message = None

    return render(request, 'support.html', {'form': form, 'success_message': success_message})
        
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
