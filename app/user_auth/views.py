from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Verifica se todos campos foram preenchidos
    if any([username, email, password]) is None:
        return render(request, "register.html", {"error": "Preencha todos os campos"})

    exist_email = User.objects.filter(email=email).first()
    exist_username = User.objects.filter(username=username).first()

    # Verifica se o email ou nome já existem no banco de dados
    if exist_email:
        return render(request, "register.html", {"error": "Email em uso, tente outro."})
    if exist_username:
        return render(request, "register.html", {"error": "Nome de usuário em uso, tente outro."})

    # Cria registro no banco
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return render(request, "register.html", {"success": "Usuário registrado com sucesso!"})
    


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request=request, username=username, password=password)
        # Faz login caso o user esteja certo
        if user:
            login_django(request, user)
            return HttpResponseRedirect(reverse("home:home_page"))
        # Warning de erro
        else:
            return render(request, "login.html", {"error": "Login inválido"})