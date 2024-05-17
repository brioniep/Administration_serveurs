from django.db import models

# Create your models here.


class Serveurs(models.Model):
    nom_serveurs = models.CharField(max_length=100, blank=True) 
    type_serveurs = models.CharField(max_length=100, blank=True) # !!! ATENTION LIAISON !!!
    nombre_processeurs = models.CharField(max_length=100, blank=True) # !!! ATENTION LIAISON !!!
    capacite_memoire = models.CharField(max_length=100, blank=True)
    capacite_stockage = models.CharField(max_length=100, blank=True)
    
    
    
class Type_serveurs(models.Model):
    type = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    
    
    
class Utilisateurs(models.Model):
    nom_utilisateurs = models.CharField(max_length=100, blank=True)
    prenom = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    
    
class Services(models.Model):
    nom_services = models.CharField(max_length=100, blank=True)
    date_lancement = models.CharField(max_length=100, blank=True)
    espace_memoire_utilise = models.CharField(max_length=100, blank=True)
    memoire_vive_necessaire = models.CharField(max_length=100, blank=True)
    serveur_de_lancement = models.CharField(max_length=100, blank=True)
    
    
    
class Applications(models.Model):
    nom_applications = models.CharField(max_length=100, blank=True)
    logo_utilisateur = models.CharField(max_length=100, blank=True)
    utilisateur = models.CharField(max_length=100, blank=True)
    
    


# class Usage_ressources(models.Model):
