from django.urls import path
from . import views

app_name = 'nnf'
urlpatterns = [
    # post views
    path('', views.liste_navires, name='liste_navires'),
    path('navire/<int:id>', views.detail_navire, name='detail_navire'),
    path('navire/ajout', views.ajout_navire, name='ajout_navire'),
    path('navire/modif/<int:id>', views.modifier_navire, name='modifier_navire'),
    path('navire/supp/<int:id>', views.supprimer_navire, name='supprimer_navire'),
    path('personnes', views.liste_personnes, name='liste_personnes'),
    path('personne/<int:id>', views.detail_personne, name='detail_personne'),
    path('personne/ajout', views.ajout_personne, name='ajout_personne'),
    path('personne/modif/<int:id>', views.modifier_personne, name='modifier_personne'),
    path('personne/supp/<int:id>', views.supprimer_personne, name='supprimer_personne'),
    path('proprietaires', views.liste_proprietaires, name='liste_proprietaires'),
    path('proprietaire/<int:id>', views.detail_proprietaire, name='detail_proprietaire'),
    path('proprietaire/ajout', views.ajout_proprietaire, name='ajout_proprietaire'),
    path('proprietaire/modif/<int:id>', views.modifier_proprietaire, name='modifier_proprietaire'),
    path('proprietaire/supp/<int:id>', views.supprimer_proprietaire, name='supprimer_proprietaire'),
    path('armateurs', views.liste_armateurs, name='liste_armateurs'),
    path('armateur/<int:id>', views.detail_armateur, name='detail_armateur'),
    path('armateur/ajout', views.ajout_armateur, name='ajout_armateur'),
    path('armateur/modif/<int:id>', views.modifier_armateur, name='modifier_armateur'),
    path('armateur/supp/<int:id>', views.supprimer_armateur, name='supprimer_armateur'),
    path('traversee/<int:navire_id>', views.ajout_traversee, name='ajout_traversee'),
    path('traversee/modif/<int:id>', views.modifier_traversee, name='modifier_traversee'),
    path('traversee/supp/<int:id>', views.supprimer_traversee, name='supprimer_traversee'),
]
