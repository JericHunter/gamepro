from django.shortcuts import render
from django.http import HttpResponse

from games.models import Game


    def index(request):
        """ GET a list of Games. """
        games = Game.objects.all()
        # upcoming = Page.objects.filter(date__gte=now).order_by('date')
        return render(request, 'game_list.html', {
          'games': games
        })
