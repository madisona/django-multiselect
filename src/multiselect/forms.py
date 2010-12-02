
from django import forms
from multiselect.fields import MultipleChoiceField
from multiselect import models

class SelectForm(forms.Form):
    CHOICES = (('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'))
    choices = MultipleChoiceField(choices=CHOICES)

class ModelSelectForm(forms.ModelForm):
    class Meta:
        model = models.SampleModel