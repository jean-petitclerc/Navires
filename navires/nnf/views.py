from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Navire, Personne, Proprietaire, Armateur, Traversee
from .forms import (FormNavire, FormPersonne, FormProprietaire, FormArmateur, FormTraversee, FormConfirmation)

import datetime


def creer_date(annee, mois, jour):
    try:
        d = datetime.datetime(annee, mois, jour)
        date = d.date()
        return date
    except:
        return None


def home(request):
    return render(request, 'index.html')


def liste_navires(request):
    navires = Navire.objects.all()
    return render(request,
                 'navires/liste.html',
                 {'navires': navires})


def detail_navire(request, id):
    try:
        navire = Navire.objects.get(id=id)
    except Navire.DoesNotExist:
        raise Http404("Le navire n'est pas retrouvé.")
    return render(request,
                  'navires/detail.html',
                  {'navire': navire})


def ajout_navire(request):
    if request.method == 'GET':
        form = FormNavire()
        return render(request, 'navires/ajout.html',
                    {'form': form})
    else:
        try:
            form = FormNavire(request.POST)
            navire = form.save(commit=False)
            navire.save()
            messages.success(request, 'Le navire a été ajouté.')
            return redirect('nnf:liste_navires')
        except ValueError:
            return render(request, 'navires/ajout.html',
                          {'form':FormNavire(), 'error':'Données invalides.'})


def modifier_navire(request, id):
    navire = get_object_or_404(Navire, id=id)
    traversees = Traversee.objects.filter(navire_id=id)
    if request.method == 'GET':
        form = FormNavire(instance=navire)
        return render(request, 'navires/modif.html',
                    {'form':form, 'navire': navire, 'traversees': traversees})
    else:
        try:
            form = FormNavire(request.POST, instance=navire)
            navire = form.save(commit=False)
            navire.save()
            messages.success(request, 'Le navire a été modifié.')
            return redirect('nnf:liste_navires')
        except ValueError:
            return render(request, 'navires/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def supprimer_navire(request, id):
    if request.method == 'GET':
        try:
            navire = Navire.objects.get(id=id)
            return render(request, 'navires/supp.html',
                          {'form':FormConfirmation, 'navire': navire})
        except Navire.DoesNotExist:
            raise Http404("Le navire n'a pas été retrouvé.")
    else:
        try:
            form = FormConfirmation(request.POST)
            navire = Navire.objects.get(id=id)
            navire.delete()
            messages.success(request, 'Le navire a été supprimé.')
            return redirect('nnf:liste_navires')
        except Navire.DoesNotExist:
            raise Http404("Le navire n'a pas été retrouvé.")
        except ValueError:
            return render(request, 'navires/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})


def liste_personnes(request):
    personnes = Personne.objects.all()
    return render(request,
                 'personnes/liste.html',
                 {'personnes': personnes})


def detail_personne(request, id):
    try:
        personne = Personne.objects.get(id=id)
    except Personne.DoesNotExist:
        raise Http404("La personne n'est pas retrouvée.")
    return render(request,
                  'personnes/detail.html',
                  {'personne': personne})


def ajout_personne(request):
    if request.method == 'GET':
        print("get")
        return render(request, 'personnes/ajout.html',
                      {'form':FormPersonne})
    else:
        print("post")
        try:
            form = FormPersonne(request.POST)
            p = form.save(commit=False)
            p.naissance_date = creer_date(p.naissance_annee, p.naissance_mois, p.naissance_jour)
            p.deces_date = creer_date(p.deces_annee, p.deces_mois, p.deces_jour)
            p.save()
            messages.success(request, 'La personne a été ajoutée.')
            return redirect('nnf:liste_personnes')
        except ValueError:
            return render(request, 'personnes/ajout.html',
                          {'form':FormPersonne(), 'error':'Données invalides.'})


def modifier_personne(request, id):
    p = get_object_or_404(Personne, id=id)
    if request.method == 'GET':
        form = FormPersonne(instance=p)
        return render(request, 'personnes/modif.html',
                    {'form':form, 'personne': p})
    else:
        try:
            form = FormPersonne(request.POST, instance=p)
            p = form.save(commit=False)
            p.naissance_date = creer_date(p.naissance_annee, p.naissance_mois, p.naissance_jour)
            p.deces_date = creer_date(p.deces_annee, p.deces_mois, p.deces_jour)
            p.save()
            messages.success(request, 'La personne a été modifiée.')
            return redirect('nnf:liste_personnes')
        except ValueError:
            return render(request, 'personnes/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def supprimer_personne(request, id):
    if request.method == 'GET':
        try:
            p = Personne.objects.get(id=id)
            return render(request, 'personnes/supp.html',
                          {'form':FormConfirmation, 'personne': p})
        except Personne.DoesNotExist:
            raise Http404("La personne n'a pas été retrouvée.")
    else:
        try:
            form = FormConfirmation(request.POST)
            p = Personne.objects.get(id=id)
            p.delete()
            messages.success(request, 'La personne a été supprimée.')
            return redirect('nnf:liste_personnes')
        except Personne.DoesNotExist:
            raise Http404("La personne n'a pas été retrouvée.")
        except ValueError:
            return render(request, 'personnes/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})


def liste_proprietaires(request):
    proprietaires = Proprietaire.objects.all()
    return render(request,
                 'proprietaires/liste.html',
                 {'proprietaires': proprietaires})


def detail_proprietaire(request, id):
    try:
        proprietaire = Proprietaire.objects.get(id=id)
        navires = Navire.objects.filter(proprietaire = proprietaire)
    except Proprietaire.DoesNotExist:
        raise Http404("Le propriétaire n'est pas retrouvé.")
    return render(request,
                  'proprietaires/detail.html',
                  {'proprietaire': proprietaire,
                   'navires': navires})


def ajout_proprietaire(request):
    if request.method == 'GET':
        return render(request, 'proprietaires/ajout.html',
                    {'form':FormProprietaire})
    else:
        try:
            form = FormProprietaire(request.POST)
            proprietaire = form.save(commit=False)
            proprietaire.save()
            messages.success(request, 'Le propriétaire a été ajouté.')
            return redirect('nnf:liste_proprietaires')
        except ValueError:
            return render(request, 'proprietaire/ajout.html',
                          {'form':FormProprietaire(), 'error':'Données invalides.'})


def modifier_proprietaire(request, id):
    proprietaire = get_object_or_404(Proprietaire, id=id)
    if request.method == 'GET':
        form = FormProprietaire(instance=proprietaire)
        return render(request, 'proprietaires/modif.html',
                    {'form':form, 'proprietaire': proprietaire})
    else:
        try:
            form = FormProprietaire(request.POST, instance=proprietaire)
            proprietaire = form.save(commit=False)
            proprietaire.save()
            messages.success(request, 'Le propriétaire a été modifié.')
            return redirect('nnf:liste_proprietaires')
        except ValueError:
            return render(request, 'proprietaires/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def supprimer_proprietaire(request, id):
    if request.method == 'GET':
        try:
            proprietaire = Proprietaire.objects.get(id=id)
            return render(request, 'proprietaires/supp.html',
                          {'form':FormConfirmation, 'proprietaire': proprietaire})
        except Proprietaire.DoesNotExist:
            raise Http404("Le propriétaire n'a pas été retrouvé.")
    else:
        try:
            form = FormConfirmation(request.POST)
            proprietaire = Proprietaire.objects.get(id=id)
            proprietaire.delete()
            messages.success(request, 'Le propriétaire a été supprimé.')
            return redirect('nnf:liste_proprietaires')
        except Proprietaire.DoesNotExist:
            raise Http404("Le propriétaire n'a pas été retrouvé.")
        except ValueError:
            return render(request, 'proprietaires/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})


def liste_armateurs(request):
    armateurs = Armateur.objects.all()
    return render(request,
                 'armateurs/liste.html',
                 {'armateurs': armateurs})


def detail_armateur(request, id):
    try:
        armateur = Armateur.objects.get(id=id)
        navires = Navire.objects.filter(armateur = armateur)
    except Armateur.DoesNotExist:
        raise Http404("L'armateur n'est pas retrouvé.")
    return render(request,
                  'armateurs/detail.html',
                  {'armateur': armateur, 'navires': navires})


def ajout_armateur(request):
    if request.method == 'GET':
        return render(request, 'armateurs/ajout.html',
                    {'form':FormArmateur})
    else:
        try:
            form = FormArmateur(request.POST)
            armateur = form.save(commit=False)
            armateur.save()
            messages.success(request, "L'armateur a été ajouté.")
            return redirect('nnf:liste_armateurs')
        except ValueError:
            return render(request, 'armateur/ajout.html',
                          {'form':FormArmateur(), 'error':'Données invalides.'})


def modifier_armateur(request, id):
    armateur = get_object_or_404(Armateur, id=id)
    if request.method == 'GET':
        form = FormArmateur(instance=armateur)
        return render(request, 'armateurs/modif.html',
                    {'form':form, 'armateur': armateur})
    else:
        try:
            form = FormArmateur(request.POST, instance=armateur)
            armateur = form.save(commit=False)
            armateur.save()
            messages.success(request, "L'armateur a été modifié.")
            return redirect('nnf:liste_armateurs')
        except ValueError:
            return render(request, 'armateurs/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def supprimer_armateur(request, id):
    if request.method == 'GET':
        try:
            armateur = Armateur.objects.get(id=id)
            return render(request, 'armateurs/supp.html',
                          {'form':FormConfirmation, 'armateur': armateur})
        except Armateur.DoesNotExist:
            raise Http404("L'armateure n'a pas été retrouvé.")
    else:
        try:
            form = FormConfirmation(request.POST)
            armateur = Armateur.objects.get(id=id)
            armateur.delete()
            messages.success(request, "L'armateur a été supprimé.")
            return redirect('nnf:liste_armateurs')
        except Armateur.DoesNotExist:
            raise Http404("L'armateur n'a pas été retrouvé.")
        except ValueError:
            return render(request, 'armateurs/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})


def ajout_traversee(request, navire_id):
    navire = get_object_or_404(Navire, id=navire_id)
    if request.method == 'GET':
        form = FormTraversee()
        return render(request, 'traversees/ajout.html',
                    {'form': form, 'navire': navire})
    else:
        try:
            form = FormTraversee(request.POST)
            traversee = form.save(commit=False)
            traversee.navire_id = navire.id
            traversee.save()
            messages.success(request, 'La traversée a été ajoutée.')
            return redirect('nnf:modifier_navire', navire_id)
        except ValueError:
            return render(request, 'traversees/ajout.html',
                          {'form':FormNavire(), 'navire': navire, 'error':'Données invalides.'})


def modifier_traversee(request, id):
    traversee = get_object_or_404(Traversee, id=id)
    if request.method == 'GET':
        form = FormTraversee(instance=traversee)
        return render(request, 'traversees/modif.html',
                    {'form':form, 'traversee': traversee})
    else:
        try:
            form = FormTraversee(request.POST, instance=traversee)
            traversee = form.save(commit=False)
            traversee.save()
            messages.success(request, 'La traversée a été modifiée.')
            return redirect('nnf:modifier_navire', traversee.navire_id)
        except ValueError:
            return render(request, 'traversees/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def supprimer_traversee(request, id):
    if request.method == 'GET':
        try:
            traversee = Traversee.objects.get(id=id)
            return render(request, 'traversees/supp.html',
                          {'form':FormConfirmation, 'traversee': traversee})
        except Traversee.DoesNotExist:
            raise Http404("La traversée n'a pas été retrouvée.")
    else:
        try:
            form = FormConfirmation(request.POST)
            traversee = Traversee.objects.get(id=id)
            navire_id = traversee.navire_id
            traversee.delete()
            messages.success(request, "La traversée a été supprimée.")
            return redirect('nnf:modifier_navire', navire_id)
        except Traversee.DoesNotExist:
            raise Http404("La traversée n'a pas été retrouvée.")
        except ValueError:
            return render(request, 'traversees/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})
