from django.db import models

class Proprietaire(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.nom


class Armateur(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.nom


class Navire(models.Model):
    nom = models.CharField(max_length=100, null=False, unique=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.RESTRICT, related_name='liste_navires', null=True, default=None)
    armateur = models.ForeignKey(Armateur, on_delete=models.RESTRICT, related_name='liste_navires', null=True, default=None)
    tonnage = models.IntegerField(null=True, default=0)


class Personne(models.Model):
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
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

    def __str__(self):
        return self.nom + ', ' + self.prenom


class Traversee(models.Model):
    navire = models.ForeignKey(Navire, on_delete=models.RESTRICT, related_name='a_fait', null=False)
    maitre = models.ForeignKey(Personne, on_delete=models.RESTRICT, related_name='est_maitre_de', null=True, default=None)
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
    retour = models.CharField(max_length=100, null=True, blank=True, default='')
    notes_equipage_passagers = models.CharField(max_length=2048, null=True, blank=True, default='')
    observations = models.CharField(max_length=2048, null=True, blank=True, default='')
    nb_autres_navires = models.SmallIntegerField(null=False, default=0)

    def __str__(self):
        return self.navire.nom + '-' + str(self.depart_annee) + '-' + self.depart_lieu


class Voyage(models.Model):
    CHOIX_ROLE = [
        (0, "Indéfini"),
        (1, "Maître"),
        (2, "Capitaine"),
        (3, "Pilote"),
        (4, "Marin"),
        (5, "Passager"),
    ]
    personne = models.ForeignKey(Personne, on_delete=models.RESTRICT, related_name='voyage_effectue', null=False)
    annee = models.SmallIntegerField(null=True, blank=True, default='')
    sequence = models.SmallIntegerField(null=False, default=1)
    destination = models.CharField(max_length=100, null=True, blank=True, default='')
    navire_nom = models.CharField(max_length=100, null=True, blank=True, default='')
    traversee = models.ForeignKey(Traversee, on_delete=models.RESTRICT, related_name='liste_passagers', null=True, default=None)
    role = models.SmallIntegerField(null=False, default=0, choices=CHOIX_ROLE)
    uk = models.UniqueConstraint(name='voyage_uk', fields=["personne_id", "annee", "sequence"])
