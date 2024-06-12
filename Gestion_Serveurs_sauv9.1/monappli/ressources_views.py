from django.shortcuts import render, HttpResponseRedirect
from .forms import RessourcesForm,CSVUploadForm
from . import models
from django.http import FileResponse
import csv
from django.core.files.storage import FileSystemStorage

def index(request):
    liste = list(models.Ressources.objects.all())
    return render(request,"Ressources/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = RessourcesForm(request)
        return render(request, "Ressources/ajout.html", {"form" : form})
    else : 
        form = RessourcesForm
        return render(request, "Ressources/ajout.html", {"form" : form})




def traitement(request) :
    
    rform = RessourcesForm(request.POST)
    
    if rform.is_valid():
        Ressources = rform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexressources/")
    else:
        return render(request, 'Ressources/ajout.html', {"form" : rform})
    
    
    



def affiche(request, id):
    Ressources = models.Ressources.objects.get(pk = id)
    return render(request, "Ressources/affiche.html", {"Ressources" : Ressources})






def update(request, id):
    Ressources = models.Ressources.objects.get(pk = id)
    form = RessourcesForm(Ressources.dico())
    return render(request, "Ressources/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id,):
    rform = RessourcesForm(request.POST)
    
    if rform.is_valid():
        Ressources = rform.save(commit = False)
        Ressources.id = id
        Ressources.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexressources/")
    else:
        return render(request, 'Ressources/ajout.html', {"form":rform, "id":id})
    
    
def delete(request, id):
    Ressources = models.Ressources.objects.get(pk = id)
    Ressources.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indexressources/")

from django.shortcuts import render, redirect
import csv
import io

def Index(request):
    Ressources = Ressources.objects.all()
    
def ajout_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        file_path = fs.path(filename)

        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Ressources, _ =Ressources.objects.get_or_create(nom=row['liens_applications'])
                Ressources = Ressources.objects.create(
                    lien_applications=row['lien_applications'],
                    lien_services=row['ien_services'],
                )
        return HttpResponseRedirect('/Ressources/index.html/')
    return render(request, 'Ressources/ajout.html')


