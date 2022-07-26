from django import forms

class BusquedaFormulario(forms.Form):
    criterio = forms.CharField()