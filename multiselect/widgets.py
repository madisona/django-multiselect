
from django import forms
from django.conf import settings

class MultiSelectWidget(forms.SelectMultiple):
    css_class = 'multiselect'
    class Media:
        css = {
            'all': (
                settings.MEDIA_URL + 'css/ui.multiselect.css',
            )
        }
        js = (
            settings.MEDIA_URL + 'js/ui.multiselect.js',
        )

    def add_css_class(self, attrs):
        attrs = attrs or {}
        if 'class' in attrs:
            attrs['class'] += " %s" % self.css_class
        else:
            attrs['class'] = self.css_class
        return attrs

    def __init__(self, attrs=None):
        attrs = self.add_css_class(attrs)
        super(MultiSelectWidget, self).__init__(attrs=attrs)