
from django.forms.models import ModelMultipleChoiceField as DjangoModelMultipleChoiceField
from django.db.models.fields.related import ManyToManyField as DjangoManyToManyField
from django.forms.fields import MultipleChoiceField as DjangoMultipleChoiceField

from multiselect.widgets import MultiSelectWidget

class MultipleChoiceField(DjangoMultipleChoiceField):
    widget = MultiSelectWidget

class ModelMultipleChoiceField(DjangoModelMultipleChoiceField):
    widget = MultiSelectWidget

class ManyToManyField(DjangoManyToManyField):
    def formfield(self, **kwargs):
        kwargs['form_class'] = ModelMultipleChoiceField
        return super(ManyToManyField, self).formfield(**kwargs)

