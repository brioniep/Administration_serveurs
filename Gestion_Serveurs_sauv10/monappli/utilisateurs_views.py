from django.shortcuts import render, HttpResponseRedirect
from .forms import UtilisateursForm
from . import models

def index(request):
    liste = list(models.Utilisateurs.objects.all())
    return render(request,"Utilisateurs/index.html", {"liste" : liste})


def ajout(request) :
    if request.method == "POST":
        form = UtilisateursForm(request)
        return render(request, "Utilisateurs/ajout.html", {"form" : form})
    else : 
        form = UtilisateursForm
        return render(request, "Utilisateurs/ajout.html", {"form" : form})




def traitement(request) :
    
    uform = UtilisateursForm(request.POST)
    
    if uform.is_valid():
        Utilisateurs = uform.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexutilisateurs/")
    else:
        return render(request, 'Utilisateurs/ajout.html', {"form" : uform})
    
    
    



def affiche(request, id):
    Utilisateurs = models.Utilisateurs.objects.get(pk = id)
    return render(request, "Utilisateurs/affiche.html", {"Utilisateurs" : Utilisateurs})






def update(request, id):
    Utilisateurs = models.Utilisateurs.objects.get(pk = id)
    form = UtilisateursForm(Utilisateurs.dico())
    return render(request, "Utilisateurs/ajout.html", {"form":form, "id":id})




def updatetraitement(request, id,):
    uform = UtilisateursForm(request.POST)
    
    if uform.is_valid():
        Utilisateurs = uform.save(commit = False)
        Utilisateurs.id = id
        Utilisateurs.save()
        return HttpResponseRedirect("/Gestion_Serveurs/indexutilisateurs/")
    else:
        return render(request, 'Utilisateurs/ajout.html', {"form":uform, "id":id})
    
    
def delete(request, id):
    Utilisateurs = models.Utilisateurs.objects.get(pk = id)
    Utilisateurs.delete()
    return HttpResponseRedirect ("/Gestion_Serveurs/indexutilisateurs/")