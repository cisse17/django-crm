
from django.urls import path
from .views import home, login_user, register_user, dashboard, logout_user, ajouter_client, modifier_infos_client, voir_infos, supprimer

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_user, name="login"),
    path('register/', register_user, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout_user, name="logout"),

    path('ajouter/', ajouter_client, name="ajouter"),
    path('modifier-informations/<int:pk>', modifier_infos_client, name="modifier-informations"),

    path('voir-informations/<int:pk>', voir_infos, name="voir-informations"),
    path('supprimer-informations/<int:pk>', supprimer, name="supprimer-informations"),
]
