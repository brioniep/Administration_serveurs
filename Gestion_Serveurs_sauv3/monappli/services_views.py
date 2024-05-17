from django.shortcuts import render, HttpResponseRedirect
from .forms import ServicesForm
from . import models


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




def updatetraitement(request, id,):
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