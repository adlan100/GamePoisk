from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

GAMES = [
    "Portal 2",
    "Minecraft",
    "Half-life 2",
    "Spore",
    "Buckshot roullet"
]

def game_list(request):
    query = request.GET.get('q')
    if query:
        filtered_games = [game for game in GAMES if query.lower() in game.lower()]
    else:
        filtered_games = GAMES

    context = {'games': filtered_games}
    return render(request, 'games/game_list.html', context)
