from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Author, Book
from django.utils.translation import gettext_lazy as _


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
        help_texts = {
            'name': _('The Old Man and the Sea'),
            'description': _('Is a novella written by the American author Ernest Hemingway in 1951'),
            'count': _('2')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Book'))
