from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from games.models import Game

def index(request):
    template = loader.get_template('trying.html')
    context = {
        'starwars' : Game.objects.get(id=1),
        'sekiro' : Game.objects.get(id=2),
        'dmc' : Game.objects.get(id=3),
        'apex' : Game.objects.get(id=4),
        'mkxi' : Game.objects.get(id=5),
        'dstranding' : Game.objects.get(id=6),
        'tdv2' : Game.objects.get(id=7),
        'daysgone' : Game.objects.get(id=8),
        'borderlands' : Game.objects.get(id=9),
        'anthem' : Game.objects.get(id=10),
        'outerworlds' : Game.objects.get(id=11),
        'codmw' : Game.objects.get(id=12),
    }
    return HttpResponse(template.render(context, request))
#
# def game(request, game_id):
#     try:
#         gme = Game.objects.get(id=game_id)
#     except Game.DoesNotExist:
#         gme = None
#
#     template = loader.get_template('game_list.html')
#     context = {
#         'game': gme
#     }
#     return HttpResponse(template.render(context, request))
