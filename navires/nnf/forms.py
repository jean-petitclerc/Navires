from django import forms
from django.forms import Form, ModelForm, Textarea, NumberInput
from .models import Navire, Personne, Proprietaire, Armateur, Traversee, Voyage

class FormNavire(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['proprietaire'] = forms.ModelChoiceField(queryset=Proprietaire.objects.all(), empty_label="(Proprio inconnu)", required=False )
        self.fields['armateur'] = forms.ModelChoiceField(queryset=Armateur.objects.all(), empty_label="(Armateur inconnu)", required=False )
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['proprietaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['armateur'].widget.attrs.update({'class': 'form-control'})
        self.fields['tonnage'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Navire
        fields = ['nom','proprietaire','armateur','tonnage']
        labels = {'nom': ('Nom'), 'proprietaire': ('Propriétaire'), 'armateur': ('Armateur'), 'tonnage': ('Tonnage (Tx)')}


class FormModifNavire(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['proprietaire'] = forms.ModelChoiceField(queryset=Proprietaire.objects.all(), empty_label="(Proprio inconnu)", required=False )
        self.fields['armateur'] = forms.ModelChoiceField(queryset=Armateur.objects.all(), empty_label="(Armateur inconnu)", required=False )
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['proprietaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['armateur'].widget.attrs.update({'class': 'form-control'})
        self.fields['tonnage'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Navire
        fields = ['nom','proprietaire','armateur','tonnage']
        labels = {'nom': ('Nom'), 'proprietaire': ('Propriétaire'), 'armateur': ('Armateur'), 'tonnage': ('Tonnage (Tx)')}


class FormPersonne(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['prenom'].widget.attrs.update({'class': 'form-control'})
        self.fields['titre'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['note_biographique'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Personne
        fields = ['nom','prenom','titre','naissance_annee', 'naissance_mois', 'naissance_jour', 'naissance_lieu',
                  'deces_annee', 'deces_mois', 'deces_jour', 'deces_lieu', 'note_biographique']
        labels = {'nom': ('Nom'), 'prenom': ('Prénom'), 'titre': ('Titre'),
                  'naissance_annee': ('Année de naissance'), 'naissance_mois': ('Mois de naissance'), 'naissance_jour': ('Jour du mois de la naissance'),
                  'naissance_lieu': ('Lieu de naissance'),
                  'deces_annee': ('Année de décès'), 'deces_mois': ('Mois de décès'), 'deces_jour': ('Jour du mois du décès'),
                  'deces_lieu': ('Lieu de décès'), 'note_biographique': ('Note biographique')}
        widgets = {
            'note_biographique': Textarea(attrs={'rows': 8}),
        }

        def clean_titre(self):
            return self.cleaned_data['titre'] or None

        def clean_naissance_annee(self):
            return self.cleaned_data['naissance_annee'] or None

        def clean_note_biographique(self):
            return self.cleaned_data['note_biographique'] or None


class FormModifPersonne(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['prenom'].widget.attrs.update({'class': 'form-control'})
        self.fields['titre'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['naissance_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['deces_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['note_biographique'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Personne
        fields = ['nom','prenom','titre','naissance_annee', 'naissance_mois', 'naissance_jour', 'naissance_lieu',
                  'deces_annee', 'deces_mois', 'deces_jour', 'deces_lieu', 'note_biographique']
        labels = {'nom': ('Nom'), 'prenom': ('Prénom'), 'titre': ('Titre'),
                  'naissance_annee': ('Année de naissance'), 'naissance_mois': ('Mois de naissance'), 'naissance_jour': ('Jour du mois de la naissance'),
                  'naissance_lieu': ('Lieu de naissance'),
                  'deces_annee': ('Année de décès'), 'deces_mois': ('Mois de décès'), 'deces_jour': ('Jour du mois du décès'),
                  'deces_lieu': ('Lieu de décès'), 'note_biographique': ('Note biographique')}
        widgets = {
            'note_biographique': Textarea(attrs={'rows': 8}),
        }

        def clean_titre(self):
            return self.cleaned_data['titre'] or None

        def clean_naissance_annee(self):
            return self.cleaned_data['naissance_annee'] or None

        def clean_note_biographique(self):
            return self.cleaned_data['note_biographique'] or None


class FormProprietaire(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Proprietaire
        fields = ['nom']
        labels = {'nom': ('Nom')}


class FormModifProprietaire(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Proprietaire
        fields = ['nom',]
        labels = {'nom': ('Nom')}


class FormArmateur(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Armateur
        fields = ['nom']
        labels = {'nom': ('Nom')}


class FormModifArmateur(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Armateur
        fields = ['nom',]
        labels = {'nom': ('Nom')}


class FormTraversee(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['maitre'] = forms.ModelChoiceField(queryset=Personne.objects.all().order_by('nom'), empty_label="(Maître inconnu)", required=False)
        self.fields['maitre'].widget.attrs.update({'class': 'form-control'})
        self.fields['objectif'].widget.attrs.update({'class': 'form-control'})
        self.fields['depart_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['depart_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['depart_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['depart_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrivee_annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrivee_mois'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrivee_jour'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrivee_lieu'].widget.attrs.update({'class': 'form-control'})
        self.fields['retour'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes_equipage_passagers'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations'].widget.attrs.update({'class': 'form-control'})
        self.fields['nb_autres_navires'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Traversee
        fields = ['maitre','objectif','depart_annee', 'depart_mois', 'depart_jour', 'depart_lieu',
                  'arrivee_annee', 'arrivee_mois', 'arrivee_jour', 'arrivee_lieu', 'retour',
                  'notes_equipage_passagers','observations', 'nb_autres_navires']
        labels = {'maitre': ('Maître'), 'objectif': ('Objectif'),
                  'depart_annee': ('Année de départ'), 'depart_mois': ('Mois de départ'), 'depart_jour': ('Jour du départ'),
                  'depart_lieu': ('Lieu de départ'),
                  'arrivee_annee': ("Année d'arrivée"), 'arrivee_mois': ("Mois d'arrivée"), 'arrivee_jour': ("Jour d'arrivée"),
                  'arrivee_lieu': ("Lieu d'arrivée"), 'retour': ('Retour'), 'notes_equipage_passagers': ("Notes équipage/passagers"),
                  'observations': ("Observations"), 'nb_autres_navires': ("Nombre d'autres navires dans l'expédition")}
        widgets = {
            'notes_equipage_passagers': Textarea(attrs={'rows': 8}),
            'observations': Textarea(attrs={'rows': 8}),
        }


class FormVoyage(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['traversee'] = forms.ModelChoiceField(queryset=Traversee.objects.all(), empty_label="(inconnue)", required=False)
        self.fields['annee'].widget.attrs.update({'class': 'form-control'})
        self.fields['sequence'].widget.attrs.update({'class': 'form-control'})
        self.fields['destination'].widget.attrs.update({'class': 'form-control'})
        self.fields['navire_nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['traversee'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Voyage
        fields = ['annee','sequence','destination', 'navire_nom', 'traversee', 'role']
        labels = {'annee': ('Année'), 'sequence': ('Séquence'),
                  'destination': ('Destination'), 'navire_nom': ('Nom du navire'),
                  'traversee': ('Traversée'), 'role': ('Rôle')}
        widgets = {
            'sequence': NumberInput(),
        }


class FormConfirmation(Form):
    dummy = forms.CharField()

