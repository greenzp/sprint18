from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Author
from django.utils.translation import gettext_lazy as _


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
        help_texts = {
            'name': _('John'),
            'surname': _('London'),
            'patronymic': _('Griffith')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save author'))
