from django.shortcuts import render, HttpResponseRedirect
from .forms import ServicesForm
from . import models
from io import BytesIO


def index(request):
    liste = list(models.Services.objects.all())
    return render(request,"Services/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = ServicesForm(request)
        return render(request, "Services/ajout.html", {"form" : form})
    else : 
        form = ServicesForm
        return render(request, "Services/ajout.html", {"form" : form})




def traitement(request) :
    
    seform = ServicesForm(request.POST)
    if seform.is_valid():
        Services = seform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexservices/")
    else:
        return render(request, 'Services/ajout.html', {"form" : seform})
    

   
    



def affiche(request, id):
    Services = models.Services.objects.get(pk = id)
    return render(request, "Services/affiche.html", {"Services" : Services})






def update(request, id):
    Services = models.Services.objects.get(pk = id)
    form = ServicesForm(Services.dico())
    return render(request, "Services/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id):
    seform = ServicesForm(request.POST)
    
    if seform.is_valid():
        Services = seform.save(commit = False)
        Services.id = id
        Services.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexservices/")
    else:
        return render(request, 'Services/ajout.html', {"form":seform, "id":id})
    
    
def delete(request, id):
    Services = models.Services.objects.get(pk = id)
    Services.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indexservices/")



from django.http import HttpResponse, FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.pdfgen import canvas
from .models import Services, Serveurs  # Assurez-vous que le modèle Services est correctement importé

def generate_pdf(request, id):
    # Créer un objet HttpResponse avec le type de contenu PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="service.pdf"'

    # Créer un canvas pour le PDF
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Définir la position initiale
    y_position = height - 200
    p.setFont("Helvetica", 12)

    # Récupérer les données des services
    liste_services=[]
    if id:
        serveur_ids = [id] # supposer que les IDs sont séparés par des virgules
        serveurs = Serveurs.objects.filter(id__in=serveur_ids)
        liste_services = Services.objects.filter(serveur_de_lancement__in=serveurs)

    else:
        serveurs = Serveurs.objects.all()
        liste_services = Services.objects.all()


    # Écrire les données des services dans le PDF
    for service in liste_services:
        p.drawString(100, y_position, f"nom_services: {service.nom_services}")
        y_position -= 15
        p.drawString(100, y_position, f"nom_serveurs: {service.serveur_de_lancement}")
        y_position -= 15

        # Si l'espace vertical est insuffisant, ajouter une nouvelle page
        if y_position < 50:
            p.showPage()
            y_position = height - 50

    # Finaliser le PDF
    p.showPage()
    p.save()
    return response

