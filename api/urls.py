from django.urls import path
from . import views
from api.views import index


urlpatterns = [
    path('game/', views.index, name='game'),
]
