from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Navire, Personne, Proprietaire, Armateur, Traversee, Autre_Navire_Traversee, Voyage
from .forms import (FormNavire, FormPersonne, FormProprietaire, FormArmateur, FormTraversee, FormVoyage, FormAutreNavireTraversee, FormConfirmation)

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
    navires = Navire.objects.all().order_by('nom')
    return render(request,
                 'navires/liste.html',
                 {'navires': navires})


def detail_navire(request, id):
    try:
        navire = Navire.objects.get(id=id)
        traversees = Traversee.objects.filter(navire_id=navire.id)
    except Navire.DoesNotExist:
        raise Http404("Le navire n'est pas retrouvé.")
    return render(request,
                  'navires/detail.html',
                  {'navire': navire, 'traversees': traversees})


@login_required
def ajout_navire(request):
    if request.method == 'GET':
        form = FormNavire()
        return render(request, 'navires/ajout.html',
                    {'form': form})
    else:
        try:
            form = FormNavire(request.POST)
            navire = form.save(commit=False)
            navire.aud_crt_user = request.user
            navire.save()
            messages.success(request, 'Le navire a été ajouté.')
            return redirect('nnf:liste_navires')
        except ValueError:
            return render(request, 'navires/ajout.html',
                          {'form':FormNavire(), 'error':'Données invalides.'})


@login_required
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
            navire.aud_upd_user = request.user
            navire.save()
            messages.success(request, 'Le navire a été modifié.')
            return redirect('nnf:liste_navires')
        except ValueError:
            return render(request, 'navires/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
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
    personnes = Personne.objects.all().order_by('nom', 'prenom')
    return render(request,
                 'personnes/liste.html',
                 {'personnes': personnes, 'liste': 'de toutes les personnes'})


def liste_gens_de_mer(request):
    personnes = Personne.objects.all().filter(liste=5).order_by('nom', 'prenom')
    return render(request,
                 'personnes/liste.html',
                 {'personnes': personnes, 'liste': 'des gens de mer'})


def detail_personne(request, id):
    try:
        personne = Personne.objects.get(id=id)
        voyages = Voyage.objects.filter(personne_id=personne.id)
    except Personne.DoesNotExist:
        raise Http404("La personne n'est pas retrouvée.")
    return render(request,
                  'personnes/detail.html',
                  {'personne': personne, 'voyages': voyages})


@login_required
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
            p.aud_crt_user = request.user
            p.save()
            messages.success(request, 'La personne a été ajoutée.')
            return redirect('nnf:modifier_personne_alt', p.id)
        except ValueError:
            return render(request, 'personnes/ajout.html',
                          {'form':FormPersonne(), 'error':'Données invalides.'})


@login_required
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
            p.aud_upd_user = request.user
            p.save()
            messages.success(request, 'La personne a été modifiée.')
            return redirect('nnf:liste_personnes')
        except ValueError:
            return render(request, 'personnes/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
def modifier_personne_alt(request, id):
    personne = get_object_or_404(Personne, id=id)
    voyages = Voyage.objects.filter(personne_id=id)
    return render(request,
                 'personnes/modif2.html',
                 {'personne': personne, 'voyages': voyages})


@login_required
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
    proprietaires = Proprietaire.objects.all().order_by('nom')
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


@login_required
def ajout_proprietaire(request):
    if request.method == 'GET':
        return render(request, 'proprietaires/ajout.html',
                    {'form':FormProprietaire})
    else:
        try:
            form = FormProprietaire(request.POST)
            proprietaire = form.save(commit=False)
            proprietaire.aud_crt_user = request.user
            proprietaire.save()
            messages.success(request, 'Le propriétaire a été ajouté.')
            return redirect('nnf:liste_proprietaires')
        except ValueError:
            return render(request, 'proprietaire/ajout.html',
                          {'form':FormProprietaire(), 'error':'Données invalides.'})


@login_required
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
            proprietaire.aud_upd_user = request.user
            proprietaire.save()
            messages.success(request, 'Le propriétaire a été modifié.')
            return redirect('nnf:liste_proprietaires')
        except ValueError:
            return render(request, 'proprietaires/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
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
    armateurs = Armateur.objects.all().order_by('nom')
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


@login_required
def ajout_armateur(request):
    if request.method == 'GET':
        return render(request, 'armateurs/ajout.html',
                    {'form':FormArmateur})
    else:
        try:
            form = FormArmateur(request.POST)
            armateur = form.save(commit=False)
            armateur.aud_crt_user = request.user
            armateur.save()
            messages.success(request, "L'armateur a été ajouté.")
            return redirect('nnf:liste_armateurs')
        except ValueError:
            return render(request, 'armateur/ajout.html',
                          {'form':FormArmateur(), 'error':'Données invalides.'})


@login_required
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
            armateur.aud_upd_user = request.user
            armateur.save()
            messages.success(request, "L'armateur a été modifié.")
            return redirect('nnf:liste_armateurs')
        except ValueError:
            return render(request, 'armateurs/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
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


def liste_traversees(request):
    traversees = Traversee.objects.all().order_by('depart_annee')
    return render(request,
                 'traversees/liste.html',
                 {'traversees': traversees})


def detail_traversee(request, id):
    try:
        traversee = Traversee.objects.get(id=id)
        passagers = traversee.liste_passagers.all()
    except Traversee.DoesNotExist:
        raise Http404("La traversée n'est pas retrouvée.")
    return render(request,
                  'traversees/detail.html',
                  {'traversee': traversee, 'passagers': passagers})


@login_required
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
            traversee.aud_crt_user = request.user
            traversee.save()
            messages.success(request, 'La traversée a été ajoutée.')
            return redirect('nnf:modifier_navire', navire_id)
        except ValueError:
            return render(request, 'traversees/ajout.html',
                          {'form':FormNavire(), 'navire': navire, 'error':'Données invalides.'})


@login_required
def modifier_traversee(request, id):
    traversee = get_object_or_404(Traversee, id=id)
    if request.method == 'GET':
        form = FormTraversee(instance=traversee)
        #autres_navires = traversee.comportait_aussi.all()
        return render(request, 'traversees/modif.html',
                    {'form':form, 'traversee': traversee})
    else:
        try:
            form = FormTraversee(request.POST, instance=traversee)
            traversee = form.save(commit=False)
            traversee.aud_upd_user = request.user
            traversee.save()
            messages.success(request, 'La traversée a été modifiée.')
            return redirect('nnf:modifier_navire', traversee.navire_id)
        except ValueError:
            return render(request, 'traversees/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
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


def detail_autre_navire_traversee(request, id):
    try:
        ant = Autre_Navire_Traversee.objects.get(id=id)
    except Autre_Navire_Traversee.DoesNotExist:
        raise Http404("Le navire de la traversée n'est pas retrouvé.")
    return render(request,
                  'autre_navire_traversee/detail.html',
                  {'ant': ant})


@login_required
def ajout_autre_navire_traversee(request, traversee_id):
    traversee = get_object_or_404(Traversee, id=traversee_id)
    if request.method == 'GET':
        form = FormAutreNavireTraversee()
        return render(request, 'autre_navire_traversee/ajout.html',
                    {'form': form, 'traversee': traversee})
    else:
        try:
            form = FormAutreNavireTraversee(request.POST)
            ant = form.save(commit=False)
            ant.traversee_id = traversee.id
            ant.aud_crt_user = request.user
            ant.save()
            messages.success(request, 'Le navire a été ajouté à la traversée.')
            return redirect('nnf:modifier_traversee', traversee_id)
        except ValueError:
            return render(request, 'autre_navire_traversee/ajout.html',
                          {'form':FormAutreNavireTraversee(), 'traversee': traversee, 'error':'Données invalides.'})


@login_required
def modifier_autre_navire_traversee(request, id):
    ant = get_object_or_404(Autre_Navire_Traversee, id=id)
    if request.method == 'GET':
        form = FormAutreNavireTraversee(instance=ant)
        return render(request, 'autre_navire_traversee/modif.html',
                    {'form':form, 'ant': ant})
    else:
        try:
            form = FormAutreNavireTraversee(request.POST, instance=ant)
            ant = form.save(commit=False)
            ant.aud_upd_user = request.user
            ant.save()
            messages.success(request, 'Le navire de la traversée a été modifié.')
            return redirect('nnf:modifier_traversee', ant.traversee.id)
        except ValueError:
            return render(request, 'autre_navire_traversee/modif.html',
                          {'form':form, 'error':'Données invalides.'})


def detail_voyage(request, id):
    try:
        voyage = Voyage.objects.get(id=id)
    except Voyage.DoesNotExist:
        raise Http404("Le voyage'est pas retrouvé.")
    return render(request,
                  'voyages/detail.html',
                  {'voyage': voyage})


@login_required
def ajout_voyage(request, personne_id):
    personne = get_object_or_404(Personne, id=personne_id)
    if request.method == 'GET':
        voyage = Voyage.objects.filter(personne_id=personne.id).order_by('-sequence').first()
        if voyage:
            next_voyage_seq = voyage.sequence + 1
        else:
            next_voyage_seq = 1
        form = FormVoyage()
        form.fields['sequence'].initial = next_voyage_seq
        return render(request, 'voyages/ajout.html',
                    {'form': form, 'personne': personne})
    else:
        try:
            form = FormVoyage(request.POST)
            voyage = form.save(commit=False)
            voyage.personne_id = personne.id
            voyage.aud_crt_user = request.user
            voyage.save()
            messages.success(request, 'Le voyage a été ajouté.')
            return redirect('nnf:modifier_personne_alt', personne_id)
        except ValueError:
            return render(request, 'voyages/ajout.html',
                          {'form':FormVoyage(), 'personne': personne, 'error':'Données invalides.'})


@login_required
def modifier_voyage(request, id):
    voyage = get_object_or_404(Voyage, id=id)
    if voyage:
        print("voage")
    else:
        print("pas voyage")
    if request.method == 'GET':
        form = FormVoyage(instance=voyage)
        return render(request, 'voyages/modif.html',
                    {'form':form, 'voyage': voyage})
    else:
        try:
            form = FormVoyage(request.POST, instance=voyage)
            voyage = form.save(commit=False)
            voyage.aud_upd_user = request.user
            voyage.save()
            messages.success(request, 'Le voyage a été modifié.')
            return redirect('nnf:modifier_personne_alt', voyage.personne.id)
        except ValueError:
            return render(request, 'voyages/modif.html',
                          {'form':form, 'error':'Données invalides.'})


@login_required
def supprimer_voyage(request, id):
    if request.method == 'GET':
        try:
            voyage = Voyage.objects.get(id=id)
            return render(request, 'voyages/supp.html',
                          {'form':FormConfirmation, 'voyage': voyage})
        except Voyage.DoesNotExist:
            raise Http404("Le voyage n'a pas été retrouvé.")
    else:
        try:
            form = FormConfirmation(request.POST)
            voyage = Voyage.objects.get(id=id)
            personne_id = voyage.personne_id
            voyage.delete()
            messages.success(request, "La voyage a été supprimé.")
            return redirect('nnf:modifier_personne_alt', personne_id)
        except Voyage.DoesNotExist:
            raise Http404("Le voyage n'a pas été retrouvé.")
        except ValueError:
            return render(request, 'voyages/supp.html',
                          {'form':FormConfirmation(), 'error':'Données invalides.'})
