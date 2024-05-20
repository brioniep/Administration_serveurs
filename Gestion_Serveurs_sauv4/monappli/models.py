from django.db import models

# Create your models here.


class Serveurs(models.Model):
    nom_serveurs = models.CharField(max_length=100, blank=True) 
    type_serveurs = models.CharField(max_length=100, blank=True) # !!! ATENTION LIAISON !!!
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
    type = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        chaine = f"{self.type}"
        return chaine
    
    def dico(self):
        chaine = f"Nom : {self.Nom} ----- Description :  {self.Description} ----- Débouchés :  {self.Debouches} ----- Categorie : {self.Categories}"
        return chaine
    
    
    
class Utilisateurs(models.Model):
    nom_utilisateurs = models.CharField(max_length=100, blank=True)
    prenom = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        chaine = f"{self.nom_utilisateurs} "
        return chaine
    
    def dico(self):
        chaine = f"Nom : {self.Nom} ----- Description :  {self.Description} ----- Débouchés :  {self.Debouches} ----- Categorie : {self.Categories}"
        return chaine    
    
    
class Services(models.Model):
    nom_services = models.CharField(max_length=100, blank=True)
    date_lancement = models.CharField(max_length=100, blank=True)
    espace_memoire_utilise = models.CharField(max_length=100, blank=True)
    memoire_vive_necessaire = models.CharField(max_length=100, blank=True)
    serveur_de_lancement = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        chaine = f"{self.nom_service} "
        return chaine

    def dico(self):
        chaine = f"Nom : {self.Nom} ----- Description :  {self.Description} ----- Débouchés :  {self.Debouches} ----- Categorie : {self.Categories}"
        return chaine    
    
    
class Applications(models.Model):
    nom_applications = models.CharField(max_length=100, blank=True)
    logo_utilisateur = models.CharField(max_length=100, blank=True)
    utilisateur = models.CharField(max_length=100, blank=True)
    


# class Usage_ressources(models.Model):
