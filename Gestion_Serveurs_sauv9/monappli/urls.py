from django.urls import path
from . import views
from . import type_serveurs_views, serveurs_views, utilisateurs_views, services_views, applications_views, ressources_views

urlpatterns = [
    
    # page d'acceuil
    path('index/', views.index),
    
    # page pour les serveurs
    path('indexserveurs/',serveurs_views.index),
    path('traitementserveurs/',serveurs_views.traitement),
    path('ajoutserveurs/',serveurs_views.ajout),
    path('afficheserveurs/<int:id>/',serveurs_views.affiche),
    path('updateserveurs/<int:id>/',serveurs_views.update),
    path('updatetraitementserveurs/<int:id>/',serveurs_views.updatetraitement),
    path('deleteserveurs/<int:id>/',serveurs_views.delete),
    

    

    # page pour les types de serveurs
    path("indextype_serveurs/", type_serveurs_views.index),
    path("traitementtype_serveurs/", type_serveurs_views.traitement),
    path("ajouttype_serveurs/", type_serveurs_views.ajout),
    path("affichetype_serveurs/<int:id>/", type_serveurs_views.affiche),
    path("updatetype_serveurs/<int:id>/", type_serveurs_views.update),
    path("updatetraitementtype_serveurs/<int:id>/", type_serveurs_views.updatetraitement),
    path("deletetype_serveurs/<int:id>/", type_serveurs_views.delete),
    
    
    # page pour les utilisateurs
    path("indexutilisateurs/", utilisateurs_views.index),
    path("traitementutilisateurs/", utilisateurs_views.traitement),
    path("ajoututilisateurs/", utilisateurs_views.ajout),
    path("afficheutilisateurs/<int:id>/", utilisateurs_views.affiche),
    path("updateutilisateurs/<int:id>/", utilisateurs_views.update),
    path("updatetraitementutilisateurs/<int:id>/", utilisateurs_views.updatetraitement),
    path("deleteutilisateurs/<int:id>/", utilisateurs_views.delete),
    
    # page pour les services
    path("indexservices/", services_views.index),
    path("traitementservices/", services_views.traitement),
    path("ajoutservices/", services_views.ajout),
    path("afficheservices/<int:id>/", services_views.affiche),
    path("updateservices/<int:id>/", services_views.update),
    path("updatetraitementservices/<int:id>/", services_views.updatetraitement),
    path("deleteservices/<int:id>/", services_views.delete),
    
    # page pour les applications
    path("indexapplications/", applications_views.index),
    path("traitementapplications/", applications_views.traitement),
    path("ajoutapplications/", applications_views.ajout),
    path("afficheapplications/<int:id>/", applications_views.affiche),
    path("updateapplications/<int:id>/", applications_views.update),
    path("updatetraitementapplications/<int:id>/", applications_views.updatetraitement),
    path("deleteapplications/<int:id>/", applications_views.delete),
    
    #page pour les ressources
    path("indexressources/", ressources_views.index),
    path("traitementressources/", ressources_views.traitement),
    path("ajoutressources/", ressources_views.ajout),
    path("afficheressources/<int:id>/", ressources_views.affiche),
    path("updateressources/<int:id>/", ressources_views.update),
    path("updatetraitementressources/<int:id>/", ressources_views.updatetraitement),
    path("deleteressources/<int:id>/", ressources_views.delete),
]