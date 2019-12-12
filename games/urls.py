from django.urls import path
from games.views import GameListView
from . import views

urlpatterns = [
    path('', GameListView.as_view(), name='game-page'),
]
