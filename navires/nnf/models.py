from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Proprietaire(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)
    aud_crt_user = models.ForeignKey(User,on_delete=models.RESTRICT, related_name='proprio_creee_par', default=1)
    aud_crt_ts = models.DateTimeField(auto_now_add=True, null=True)
    aud_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT, null=True, related_name='proprio_maj_par')
    aud_upd_ts = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nom


class Armateur(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)
    aud_crt_user = models.ForeignKey(User,on_delete=models.RESTRICT, related_name='armateur_creee_par', default=1)
    aud_crt_ts = models.DateTimeField(auto_now_add=True, null=True)
    aud_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT, null=True, related_name='armateur_maj_par')
    aud_upd_ts = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nom


class Navire(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.RESTRICT, related_name='liste_navires', null=True, default=None)
    armateur = models.ForeignKey(Armateur, on_delete=models.RESTRICT, related_name='liste_navires', null=True, default=None)
    tonnage = models.IntegerField(null=True, default=0)
    aud_crt_user = models.ForeignKey(User,on_delete=models.RESTRICT, related_name='navire_creee_par', default=1)
    aud_crt_ts = models.DateTimeField(auto_now_add=True, null=True)
    aud_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT, null=True, related_name='navire_maj_par')
    aud_upd_ts = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nom


class Personne(models.Model):
    CHOIX_LISTE = [
        (0, "Indéfini"),
        (1, "Administrateurs"),
        (2, "Émigrants repassés en France"),
        (3, "Engagés"),
        (4, "Filles du roi et filles à marier"),
        (5, "Gens de Mer"),
        (6, "Marchands"),
        (7, "Militaires"),
        (8, "Religieux"),
        (9, "Volontaires et autres immigrants"),
    ]
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    variation_du_nom = models.CharField(max_length=100, null=True, blank=True, default='')
    titre = models.CharField(max_length=50, null=True, blank=True, default='')
    naissance_annee = models.SmallIntegerField(null=True, blank=True, default='')
    naissance_mois = models.SmallIntegerField(null=True, blank=True, default='')
    naissance_jour  = models.SmallIntegerField(null=True, blank=True, default='')
    naissance_date = models.DateField(null=True)
    naissance_lieu = models.CharField(max_length=100, null=True, blank=True, default='')
    deces_annee = models.SmallIntegerField(null=True, blank=True, default='')
    deces_mois = models.SmallIntegerField(null=True, blank=True, default='')
    deces_jour  = models.SmallIntegerField(null=True, blank=True, default='')
    deces_date = models.DateField(null=True)
    deces_lieu = models.CharField(max_length=100, null=True, blank=True, default='')
    note_biographique = models.CharField(max_length=2048, null=True, blank=True, default='')
    liste = models.SmallIntegerField(null=False, default=0, choices=CHOIX_LISTE)
    origine_lieu = models.CharField(max_length=100, null=True, blank=True, default='')
    aud_crt_user = models.ForeignKey(User,on_delete=models.RESTRICT, related_name='personne_creee_par', default=1)
    aud_crt_ts = models.DateTimeField(auto_now_add=True, null=True)
    aud_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT, null=True, related_name='personne_maj_par')
    aud_upd_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom + ', ' + self.prenom


class Traversee(models.Model):
    navire = models.ForeignKey(Navire, on_delete=models.RESTRICT, related_name='a_fait', null=False)
    objectif = models.CharField(max_length=50, null=True, blank=True, default='')
    depart_annee = models.SmallIntegerField(null=True, blank=True, default='')
    depart_mois = models.SmallIntegerField(null=True, blank=True, default='')
    depart_jour  = models.SmallIntegerField(null=True, blank=True, default='')
    depart_date = models.DateField(null=True)
    depart_lieu = models.CharField(max_length=100, null=True, blank=True, default='')
    arrivee_annee = models.SmallIntegerField(null=True, blank=True, default='')
    arrivee_mois = models.SmallIntegerField(null=True, blank=True, default='')
    arrivee_jour  = models.SmallIntegerField(null=True, blank=True, default='')
    arrivee_date = models.DateField(null=True)
    arrivee_lieu = models.CharField(max_length=100, null=True, blank=True, default='')
    destination = models.CharField(max_length=100, null=True, blank=True, default='')
    retour = models.CharField(max_length=100, null=True, blank=True, default='')
    notes_equipage_passagers = models.CharField(max_length=2048, null=True, blank=True, default='')
    observations = models.CharField(max_length=4096, null=True, blank=True, default='')
    nb_autres_navires = models.SmallIntegerField(null=False, default=0)
    aud_crt_user = models.ForeignKey(User,on_delete=models.RESTRICT, related_name='traversee_creee_par', default=1)
    aud_crt_ts = models.DateTimeField(auto_now_add=True, null=True)
    aud_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT, null=True, related_name='traversee_maj_par')
    aud_upd_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.navire.nom + '-' + str(self.depart_annee) + '-' + self.depart_lieu


class Autre_Navire_Traversee(models.Model):
    navire = models.ForeignKey(Navire, on_delete=models.RESTRICT, related_name='etait_dans', null=False)
    traversee = models.ForeignKey(Traversee, on_delete=models.CASCADE, related_name='comportait_aussi', null=False)
    observations = models.CharField(max_length=2048, null=True, blank=True, default='')


class Voyage(models.Model):
    CHOIX_ROLE = [
        (0, "Indéfini"),
        (2, "Capitaine"),
        (6, "Contrôleur"),
        (1, "Maître"),
        (4, "Membre d'équipage"),
        (5, "Passager"),
        (3, "Pilote"),
    ]
    personne = models.ForeignKey(Personne, on_delete=models.RESTRICT, related_name='voyage_effectue', null=False)
    annee = models.SmallIntegerField(null=True, blank=True, default='')
    sequence = models.SmallIntegerField(null=False, default=1)
    destination = models.CharField(max_length=100, null=True, blank=True, default='')
    navire_nom = models.CharField(max_length=100, null=True, blank=True, default='')
    traversee = models.ForeignKey(Traversee, on_delete=models.RESTRICT, related_name='liste_passagers', null=True, default=None)
    role = models.SmallIntegerField(null=False, default=0, choices=CHOIX_ROLE)
    uk = models.UniqueConstraint(name='voyage_uk', fields=["personne_id", "annee", "sequence"])
