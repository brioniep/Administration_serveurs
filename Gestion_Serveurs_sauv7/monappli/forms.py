from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models



class ServeursForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ['nom_serveurs', 'type_serveurs', 'nombre_processeurs', 'capacite_memoire', 'capacite_stockage']
        labels = {
            'nom_serveurs' : _('Nom du serveur'),
            'type_serveurs' : _('Type du serveur'),
            'nombre_processeurs' : _('Nombres de processeurs'),
            'capacite_memoire' : _('Capacité de mémoire (Go)'),
            'capacite_stockage' : _('Capacité de sctockage (Go)'),
        }

class Type_serveursForm(ModelForm):
    class Meta:
        model = models.Type_serveurs
        fields = ['type_srv', 'description']
        labels = {
            'type_srv' : _('Type du serveur'),
            'description' : _('Description du serveur'),
        }

class UtilisateursForm(ModelForm):
    class Meta:
        model = models.Utilisateurs
        fields = ['nom_utilisateurs', 'prenom', 'email']
        labels = {
            'nom_utilisateurs' : _("Nom de l'utilisateur"),
            'prenom' : _("Prenom de l'utilisateur"),
            'email' : _('Adresse mail @'),
        }
class ServicesForm(ModelForm):
    class Meta:
        model = models.Services
        fields = ['nom_services', 'date_lancement', 'espace_memoire_utilise', 'memoire_vive_necessaire', 'serveur_de_lancement']
        labels = {
            'nom_services' : _('Nom du service'),
            'date_lancement' : _('Date du lancement'),
            'espace_memoire_utilise' : _('Espace mémoire utilisé (Go)'),
            'memoire_vive_necessaire' : _('Mémoire vive utilisé (Go)'),
            'serveur_de_lancement' : _('Serveur de lancement'),
        }

class ApplicationsForm(ModelForm):
    class Meta:
        model = models.Applications
        fields = ['nom_applications', 'logo_utilisateur', 'utilisateur']
        labels = {
            'nom_applications' : _("Nom de l'application"),
            'logo_utilisateur' : _("Logo de l'utilisateur"),
            'utilisateur' : _("Nom de l'utilisateur"),
        }
        
        
        
class RessourcesForm(ModelForm):
    class Meta:
        model = models.Ressources
        fields = ['lien_applications', 'lien_services']
        labels = {
            'lien_applications' : _("Application séléctionner"),
            'lien_services' : _("Services(s) utilisé"),
        }