from django.shortcuts import render
from .forms import MovieForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movie

# Create your views here.
def index(request):

    if request.method !='POST':
        form=MovieForm()
    else:
        form=MovieForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaFilmes'))
            
    context={'form':form}
    return render(request,'app_principal/index.html',context)

def listaFilmes(request):
        movie=Movie.objects.order_by('date_added')
        context={'movies':movie}
        return render(request,'app_principal/listaFilmes.html',context)

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