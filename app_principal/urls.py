from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('listaFilmes', views.listaFilmes,name='listaFilmes'),
    path('descricaoFilme/<movie_id>/',views.descricaoFilme,name='descricaoFilme'),
    path('deletaFilme/<movie_id>/',views.deletaFilme,name='deletaFilme')
]
