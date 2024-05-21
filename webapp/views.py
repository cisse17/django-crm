from django.shortcuts import render, redirect
from .models import Customer

# from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm, LoginForm, AjoutInfosClient, ModifierInfosClient

def home(request):
    return render(request, 'webapp/index.html')


def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a bien été créé")
            return redirect('login')

    return render(request, 'webapp/inscription.html', {"form": form})


def login_user(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                #messages.success(request, "Vous etes connecté à votre compte")
                return redirect('dashboard')

    return render(request, 'webapp/connexion.html', {"form": form})


def logout_user(request):

    logout(request)
    messages.success(request, "Deconnecté avec succés")

    return redirect('login')

# Tableau de bord
@login_required(login_url='login')
def dashboard(request):
    infos_clients = Customer.objects.all()


    return render(request, 'webapp/dashboard.html',{'clients':infos_clients})


#____Ajouter et modifier informations clients_______


@login_required(login_url='login')
def ajouter_client(request):
    form = AjoutInfosClient()

    if request.method == 'POST':
        form = AjoutInfosClient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vous avez ajouté un nouveau client")
            return redirect("dashboard")

    return render(request, 'webapp/ajouter.html',{'form':form})


@login_required(login_url='login')
def modifier_infos_client(request, pk):

    obj = Customer.objects.get(id=pk)
    form = AjoutInfosClient(instance=obj)
    if request.method == 'POST':
         form = AjoutInfosClient(request.POST, instance=obj)

         if form.is_valid():
             form.save()
             messages.success(request, "les informations ont été modifiées avec succés")

             return redirect('dashboard')

    return render(request, 'webapp/modifier.html',{'form':form})


# Voir details des informations enregistrées
@login_required(login_url='login')
def voir_infos(request, pk):
    infos = Customer.objects.get(id=pk)

    return render(request, 'webapp/voir.html', {'infos':infos})


# supprimer inforamtions
@login_required(login_url='login')
def supprimer(request, pk):
    obj = Customer.objects.get(id=pk)
    obj.delete()
    messages.success(request, "les informations ont été supprimées")

    return redirect('dashboard')


# mdp dashborad123@    username = manager1
# dashborad123@@   manager2

# admin
# 1234567