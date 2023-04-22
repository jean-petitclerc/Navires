from django import forms
from django.forms import Form, ModelForm, Textarea
from .models import Navire, Personne, Proprietaire, Armateur

class FormAjoutNavire(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['proprietaire'] = forms.ModelChoiceField(queryset=Proprietaire.objects.all(), empty_label="(Proprio inconnu)", required=False )
        self.fields['armateur'] = forms.ModelChoiceField(queryset=Armateur.objects.all(), empty_label="(Armateur inconnue)", required=False )
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
        self.fields['proprietaire'] = forms.ModelChoiceField(queryset=Proprietaire.objects.all(), empty_label="(Sans propriétaire)", required=False )
        self.fields['armateur'] = forms.ModelChoiceField(queryset=Armateur.objects.all(), empty_label="(Armateur inconnue)", required=False )
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['proprietaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['armateur'].widget.attrs.update({'class': 'form-control'})
        self.fields['tonnage'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Navire
        fields = ['nom','proprietaire','armateur','tonnage']
        labels = {'nom': ('Nom'), 'proprietaire': ('Propriétaire'), 'armateur': ('Armateur'), 'tonnage': ('Tonnage (Tx)')}


class FormAjoutPersonne(ModelForm):
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


class FormAjoutProprietaire(ModelForm):
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


class FormAjoutArmateur(ModelForm):
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


class FormConfirmation(Form):
    dummy = forms.CharField()

