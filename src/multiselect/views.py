# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from multiselect import widgets

class SelectForm(forms.Form):
    CHOICES = (('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'))
    choice = forms.ChoiceField(widget=widgets.MultiSelectWidget(), choices=CHOICES)

def index(request):
    return render_to_response("multiselect/index.html", {'form': SelectForm()},
                              context_instance=RequestContext(request))
