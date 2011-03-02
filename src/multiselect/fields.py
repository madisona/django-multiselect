
from django.forms.models import ModelMultipleChoiceField as DjangoModelMultipleChoiceField
from django.db.models.fields.related import ManyToManyField as DjangoManyToManyField
from django.forms.fields import MultipleChoiceField as DjangoMultipleChoiceField

from multiselect.widgets import MultiSelectWidget

class MultipleChoiceField(DjangoMultipleChoiceField):
    widget = MultiSelectWidget

class ModelMultipleChoiceField(DjangoModelMultipleChoiceField):
    widget = MultiSelectWidget

    def label_from_instance(self, obj):
        if hasattr(obj, 'verbose_label'):
            return obj.verbose_label()
        return super(ModelMultipleChoiceField, self).label_from_instance(obj)

class ManyToManyField(DjangoManyToManyField):

    def __init__(self, *args, **kwargs):
        super(ManyToManyField, self).__init__(*args, **kwargs)
        self.help_text = kwargs.get("help_text", '')

    def formfield(self, **kwargs):
        kwargs['form_class'] = ModelMultipleChoiceField
        return super(ManyToManyField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^multiselect\.fields\.ManyToManyField"])
except ImportError:
    pass