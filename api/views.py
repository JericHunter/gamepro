from games.models import Game
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from api.serializers import GameSerializer
from django.shortcuts import render

def index(APIView):
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
    data = GameSerializer(context, many=True).data
    return Response(data)
