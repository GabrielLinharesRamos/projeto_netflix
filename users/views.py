from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def logout_view(request):
    """Faz logout do usuario"""
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# Create your views here.
