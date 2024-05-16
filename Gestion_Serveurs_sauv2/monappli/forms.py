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
            'capacite_memoire' : _('Capacité de mémoire'),
            'capacite_stockage' : _('Capacité de sctockage'),
        }

class Type_serveursForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ['type', 'description']
        labels = {
            'type' : _('Type du serveur'),
            'description' : _('Description du serveur'),
        }

class UtilisateursForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ['nom_utilisateurs', 'prenom', 'email']
        labels = {
            'nom_utilisateurs' : _("Nom de l'utilisateur"),
            'prenom' : _("Prenom de l'utilisateur"),
            'email' : _('Adresse mail @'),
        }
class ServicesForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ['nom_services', 'date_lancement', 'espace_memoire_utilise', 'memoire_vive_necessaire', 'serveurs_de_lancement']
        labels = {
            'nom_services' : _('Nom du service'),
            'date_lancement' : _('Date du lancement'),
            'espace_memoire_utilise' : _('Espace mémoire utilisé'),
            'memoire_vive_necessaire' : _('Mémoire vive utilisé'),
            'serveur_de_lancement' : _('Serveur de lancement'),
        }

class ApplicationForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ['nom_applications', 'logo_utilisateur', 'utilisateur']
        labels = {
            'nom_applications' : _("Nom de l'application"),
            'logo_utilisateur' : _("Logo de l'utilisateur"),
            'utilisateur' : _("Nom de l'utilisateur"),
        }