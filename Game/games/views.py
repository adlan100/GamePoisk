from django.shortcuts import render
from django.http import HttpResponse

def game_list(request):
    return render(request, 'games/game_list.html')
