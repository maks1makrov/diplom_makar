from django.forms import ModelForm

from .models import KonspectOne


class KonspectOneForm(ModelForm):
    class Meta:
        model = KonspectOne
        fields = ('ideologia', 'link', 'since', 'polit_ideologia')
