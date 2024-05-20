from django.shortcuts import render, HttpResponseRedirect
from .forms import ApplicationsForm
from . import models


def index(request):
    liste = list(models.Applications.objects.all())
    return render(request,"Applications/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = ApplicationsForm(request)
        return render(request, "Applications/ajout.html", {"form" : form})
    else : 
        form = ApplicationsForm
        return render(request, "Applications/ajout.html", {"form" : form})




def traitement(request) :
    
    aform = ApplicationsForm(request.POST)
    
    if aform.is_valid():
        Applications = aform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexapplications/")
    else:
        return render(request, 'Applications/ajout.html', {"form" : aform})
    
    
    



def affiche(request, id):
    Applications = models.Applications.objects.get(pk = id)
    return render(request, "Applications/affiche.html", {"Applications" : Applications})






def update(request, id):
    Applications = models.Applications.objects.get(pk = id)
    form = ApplicationsForm(Applications.dico())
    return render(request, "Applications/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id,):
    aform = ApplicationsForm(request.POST)
    
    if aform.is_valid():
        Applications = aform.save(commit = False)
        Applications.id = id
        Applications.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexapplications/")
    else:
        return render(request, 'Applications/ajout.html', {"form":aform, "id":id})
    
    
def delete(request, id):
    Applications = models.Applications.objects.get(pk = id)
    Applications.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indexapplications/")