from django.shortcuts import render, HttpResponseRedirect
from .forms import Type_serveursForm
from . import models

def index(request):
    liste = list(models.Type_serveurs.objects.all())
    return render(request,"Type_serveurs/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = Type_serveursForm(request)
        return render(request, "Type_serveurs/ajout.html", {"form" : form})
    else : 
        form = Type_serveursForm
        return render(request, "Type_serveurs/ajout.html", {"form" : form})




def traitement(request) :
    
    tform = Type_serveursForm(request.POST)
    
    if tform.is_valid():
        Type_serveurs = tform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indextype_serveurs/")
    else:
        return render(request, 'Type_serveurs/ajout.html', {"form" : tform})
    
    
    



def affiche(request, id):
    Type_serveurs = models.Type_serveurs.objects.get(pk = id)
    return render(request, "Type_serveurs/affiche.html", {"Serveurs" : Type_serveurs})






def update(request, id):
    Type_serveurs = models.Type_serveurs.objects.get(pk = id)
    form = Type_serveursForm(Type_serveurs.dico())
    return render(request, "Type_serveurs/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id,):
    tform = Type_serveursForm(request.POST)
    
    if tform.is_valid():
        Type_serveurs = tform.save(commit = False)
        Type_serveurs.id = id
        Type_serveurs.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indextype_serveurs/")
    else:
        return render(request, 'Type_serveurs/ajout.html', {"form":tform, "id":id})
    
    
def delete(request, id):
    Type_serveurs = models.Type_serveurs.objects.get(pk = id)
    Type_serveurs.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indextype_serveurs/")