from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('listaFilmes', views.listaFilmes,name='listaFilmes'),
    path('descricaoFilme/<movie_id>/',views.descricaoFilme,name='descricaoFilme'),
    path('deletaFilmeBanco/<movie_id>/',views.deletaFilme,name='deletaFilme'),
    path('adicionaFilmeUsuario/<movie_id>',views.add_movie_to_list,name='adicionaUser'),
    path('deletaFilmeUsuario/<movie_id>',views.add_movie_to_list,name='deletaUser')
]
