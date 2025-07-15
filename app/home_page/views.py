from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_page(request):
    if request.user.is_authenticated:
        return HttpResponse("Entrou")
    else:
        return HttpResponse("Não logado")