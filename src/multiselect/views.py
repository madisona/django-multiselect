# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response

from multiselect import forms

def index(request):
    data = {'form': forms.SelectForm(), 'modelform':forms.ModelSelectForm()}
    
    return render_to_response("multiselect/index.html", data,
                              context_instance=RequestContext(request))
