from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('starwars', views.starwars, name='starwars'),
    path('anthem', views.anthem, name='anthem'),
    path('apex', views.apex, name='apex'),
    path('borderlands', views.borderlands, name='borderlands'),
    path('codmw', views.codmw, name='codmw'),
    path('daysgone', views.daysgone, name='daysgone'),
    path('dmc', views.dmc, name='dmc'),
    path('dstranding', views.dstranding, name='dstranding'),
    path('mkxi', views.mkxi, name='mkxi'),
    path('outerworlds', views.outerworlds, name='outerworlds'),
    path('sekiro', views.sekiro, name='sekiro'),
    path('tdv2', views.tdv2, name='tdv2'),
]
