from django.shortcuts import render, HttpResponseRedirect
from .forms import ServeursForm
from . import models


def index(request):
    liste = list(models.Serveurs.objects.all())
    return render(request,"Serveurs/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = ServeursForm(request)
        return render(request, "Serveurs/ajout.html", {"form" : form})
    else : 
        form = ServeursForm
        return render(request, "Serveurs/ajout.html", {"form" : form})




def traitement(request) :
    
    sform = ServeursForm(request.POST)
    
    if sform.is_valid():
        Serveurs = sform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexserveurs/")
    else:
        return render(request, 'Serveurs/ajout.html', {"form" : sform})
    
    
    



def affiche(request, id):
    Serveurs = models.Serveurs.objects.get(pk = id)
    return render(request, "Serveurs/affiche.html", {"Serveurs" : Serveurs})






def update(request, id):
    Serveurs = models.Serveurs.objects.get(pk = id)
    form = ServeursForm(Serveurs.dico())
    return render(request, "Serveurs/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id,):
    sform = ServeursForm(request.POST)
    
    if sform.is_valid():
        Serveurs = sform.save(commit = False)
        Serveurs.id = id
        Serveurs.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexserveurs/")
    else:
        return render(request, 'Serveurs/ajout.html', {"form":sform, "id":id})
    
    
def delete(request, id):
    Serveurs = models.Serveurs.objects.get(pk = id)
    Serveurs.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indexserveurs/")





