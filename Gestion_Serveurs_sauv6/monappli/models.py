from django.db import models

# Create your models here.


class Serveurs(models.Model):
    nom_serveurs = models.CharField(max_length=100, blank=True) 
    type_serveurs = models.CharField(max_length=100, blank=True) 
    nombre_processeurs = models.CharField(max_length=100, blank=True) # !!! ATENTION LIAISON !!!
    capacite_memoire = models.CharField(max_length=100, blank=True)
    capacite_stockage = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        chaine = f"{self.nom_serveurs} "
        return chaine
    
    def dico(self):
        return {
            "nom_serveurs": self.nom_serveurs,
            "type_serveurs": self.type_serveurs,
            "nombre_processeurs": self.nombre_processeurs,
            "capacite_memoire": self.capacite_memoire,
            "capacite_stockage": self.capacite_stockage
        }

class Type_serveurs(models.Model):
    type_srv = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        chaine = f"{self.type_srv}"
        return chaine
    
    def dico(self):
        return {
            "type_srv": self.type_srv,
            "description": self.description
        }
    
    
class Utilisateurs(models.Model):
    nom_utilisateurs = models.CharField(max_length=100, blank=True)
    prenom = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        chaine = f"{self.nom_utilisateurs} "
        return chaine
    
    def dico(self):
        return {
            "nom_utilisateurs": self.nom_utilisateurs,
            "prenom": self.prenom,
            "email": self.email
        }   
    
    
class Services(models.Model):
    nom_services = models.CharField(max_length=100, blank=True)
    date_lancement = models.CharField(max_length=100, blank=True)
    espace_memoire_utilise = models.CharField(max_length=100, blank=True)
    memoire_vive_necessaire = models.CharField(max_length=100, blank=True)
    serveur_de_lancement = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        chaine = f"{self.nom_services} "
        return chaine

    def dico(self):
        return {
            "nom_services": self.nom_services,
            "date_lancement": self.date_lancement,
            "espace_memoire_utilise": self.espace_memoire_utilise,
            "memoire_vive_necessaire": self.memoire_vive_necessaire,
            "serveur_de_lancement": self.serveur_de_lancement
        } 
    
    
class Applications(models.Model):
    nom_applications = models.CharField(max_length=100, blank=True)
    logo_utilisateur = models.CharField(max_length=100, blank=True)
    utilisateur = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        chaine = f"{self.nom_applications} "
        return chaine

    


# class Usage_ressources(models.Model):
