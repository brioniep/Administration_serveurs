from django.urls import path
from . import views
from . import type_serveurs_views, serveurs_views, utilisateurs_views, services_views, applications_views

urlpatterns = [
    
    # page pour les serveurs
    path('indexserveurs/',serveurs_views.index),
    path('traitement/',serveurs_views.traitement),
    path('ajout/',serveurs_views.ajout),
    path('affiche/<int:id>/',serveurs_views.affiche),
    path('update/<int:id>/',serveurs_views.update),
    path('updatetraitement/<int:id>/',serveurs_views.updatetraitement),
    path('delete/<int:id>/',serveurs_views.delete),
    

    # page pour les types de serveurs
    path("indexformations/", type_serveurs_views.index),
    path("traitementformations/", type_serveurs_views.traitement),
    path("ajoutformations/", type_serveurs_views.ajout),
    path("afficheformations/<int:id>/", type_serveurs_views.affiche),
    path("updateformations/<int:id>/", type_serveurs_views.update),
    path("updatetraitementformations/<int:id>/", type_serveurs_views.updatetraitement),
    path("deleteformations/<int:id>/", type_serveurs_views.delete),
    
    
    # page pour les utilisateurs
    path("indexformations/", utilisateurs_views.index),
    path("traitementformations/", utilisateurs_views.traitement),
    path("ajoutformations/", utilisateurs_views.ajout),
    path("afficheformations/<int:id>/", utilisateurs_views.affiche),
    path("updateformations/<int:id>/", utilisateurs_views.update),
    path("updatetraitementformations/<int:id>/", utilisateurs_views.updatetraitement),
    path("deleteformations/<int:id>/", utilisateurs_views.delete),
    
    # page pour les services
    path("indexformations/", services_views.index),
    path("traitementformations/", services_views.traitement),
    path("ajoutformations/", services_views.ajout),
    path("afficheformations/<int:id>/", services_views.affiche),
    path("updateformations/<int:id>/", services_views.update),
    path("updatetraitementformations/<int:id>/", services_views.updatetraitement),
    path("deleteformations/<int:id>/", services_views.delete),
    
    # page pour les applications
    path("indexformations/", applications_views.index),
    path("traitementformations/", applications_views.traitement),
    path("ajoutformations/", applications_views.ajout),
    path("afficheformations/<int:id>/", applications_views.affiche),
    path("updateformations/<int:id>/", applications_views.update),
    path("updatetraitementformations/<int:id>/", applications_views.updatetraitement),
    path("deleteformations/<int:id>/", applications_views.delete),
]