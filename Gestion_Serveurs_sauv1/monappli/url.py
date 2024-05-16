from django.urls import path
from . import views
from . import formations_views

urlpatterns = [
    
    # page pour les serveurs
    path('indexcategories/', views.index),
    path('traitement/', views.traitement),
    path('ajout/', views.ajout),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    

    # page pour toutes les formations
    path("indexformations/", formations_views.index),
    path("traitementformations/", formations_views.traitement),
    path("ajoutformations/", formations_views.ajout),
    path("afficheformations/<int:id>/", formations_views.affiche),
    path("updateformations/<int:id>/", formations_views.update),
    path("updatetraitementformations/<int:id>/", formations_views.updatetraitement),
    path("deleteformations/<int:id>/", formations_views.delete),
    
]