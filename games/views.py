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

def starwars(request):
    template = loader.get_template('starwars.html')
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

def sekiro(request):
    template = loader.get_template('sekiro.html')
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
def dmc(request):
    template = loader.get_template('dmc.html')
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
def apex(request):
    template = loader.get_template('apex.html')
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
def tdv2(request):
    template = loader.get_template('tdv2.html')
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
def mkxi(request):
    template = loader.get_template('mkxi.html')
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
def dstranding(request):
    template = loader.get_template('dstranding.html')
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
def borderlands(request):
    template = loader.get_template('borderlands.html')
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
def anthem(request):
    template = loader.get_template('anthem.html')
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
def daysgone(request):
    template = loader.get_template('daysgone.html')
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
def outerworlds(request):
    template = loader.get_template('outerworlds.html')
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
def codmw(request):
    template = loader.get_template('codmw.html')
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
