from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Serveurs(models.Model):
    nom_serveurs = models.CharField(max_length=100, blank=False) 
    type_serveurs = models.ForeignKey("Type_serveurs", on_delete=models.CASCADE, blank=False) 
    nombre_processeurs = models.IntegerField(blank=False)
    capacite_memoire = models.IntegerField( blank=False)
    capacite_stockage = models.IntegerField(blank=True)
    
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
    def memoire_restante(self):
        services = self.services_set.all()
        memoire_utilisee = sum(int(service.memoire_vive_necessaire) for service in services)
        return self.capacite_memoire - memoire_utilisee
        


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
    
class Services(models.Model):
    nom_services = models.CharField(max_length=100, blank=True)
    date_lancement = models.DateField()
    espace_memoire_utilise = models.IntegerField(blank=True)
    memoire_vive_necessaire = models.IntegerField(blank=False)
    serveur_de_lancement = models.ForeignKey("Serveurs", on_delete=models.CASCADE, blank=False)
    
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
        
        
    def clean(self):
        super().clean()
        memoire_restante = self.serveur_de_lancement.memoire_restante()
        if self.memoire_vive_necessaire > memoire_restante:
            raise ValidationError("La mémoire vive nécessaire dépasse la capacité de mémoire restante sur le serveur.")
          
class Utilisateurs(models.Model):
    nom_utilisateurs = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    
    
    def __str__(self):
        chaine = f"{self.nom_utilisateurs} "
        return chaine
    
    def dico(self):
        return {
            "nom_utilisateurs": self.nom_utilisateurs,
            "prenom": self.prenom,
            "email": self.email
        }   
    
    
class Applications(models.Model):
    nom_applications = models.CharField(max_length=100, blank=True)
    logo_utilisateur = models.ImageField(upload_to='logo_utilisateur' ,blank=False,)
    utilisateur = models.ForeignKey("Utilisateurs", on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        chaine = f"{self.nom_applications}"
        return chaine
    
    def dico(self):
        return {
            "nom_applications": self.nom_applications,
            "logo_utilisateur": self.logo_utilisateur,
            "utilisateur": self.utilisateur
        } 
    


class Ressources(models.Model):
    lien_applications = models.ForeignKey("Applications", on_delete=models.CASCADE, blank=False)
    lien_services = models.ForeignKey("Services", on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        chaine = f"{self.lien_applications}"
        return chaine
    
    def dico(self):
        return {
            "lien_applications": self.lien_applications,
            "lien_services": self.lien_services
        }
        

