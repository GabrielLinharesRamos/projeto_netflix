from django.shortcuts import render,get_object_or_404
from .forms import MovieForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movie,UserMovieList
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):        
    return render(request,'app_principal/home.html')



def index(request):

    if request.method !='POST':
        form=MovieForm()
    else:
        form=MovieForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaFilmes'))
            
    context={'form':form}
    return render(request,'app_principal/cadastro.html',context)

def listaFilmes(request):
        movie=Movie.objects.order_by('date_added')
        context={'movies':movie}

        if request.user.is_authenticated:
        # Dados específicos para usuários logados
            context['movies_user'] = get_user_movies(request)

        return render(request,'app_principal/listaFilmes.html',context)

@login_required
def get_user_movies(request):
    movies_user=Movie.objects.filter(usermovielist__user=request.user)
    return movies_user

def descricaoFilme(request,movie_id):
     movie=Movie.objects.get(id=movie_id)
     context={'movie':movie}
     return render(request,'app_principal/descricaoFilme.html',context)

def deletaFilme(request,movie_id):
    movie=Movie.objects.get(id=movie_id)

    if request.method =='POST':
        movie.delete()
        return HttpResponseRedirect(reverse('listaFilmes'))
     
    context={'movie':movie}
    return render(request, 'app_principal/descricaoFilme.html', context)

@login_required
def add_movie_to_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    UserMovieList.objects.get_or_create(user=request.user, movie=movie)
    return HttpResponseRedirect(reverse('listaFilmes'))

@login_required
def remove_movie_from_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    UserMovieList.objects.filter(user=request.user, movie=movie).delete()
    return render(request,'app_principal/listaFilmes.html') 