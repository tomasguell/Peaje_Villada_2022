from django import forms
from .models import turnos


class NuevoTurno(forms.ModelForm):
    class Meta:
        model = turnos
        fields = '__all__'