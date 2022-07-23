from django import forms

class PersonaFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()