from django.shortcuts import render, HttpResponseRedirect
from .forms import RessourcesForm
from . import models

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