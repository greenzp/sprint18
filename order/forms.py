from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Order
from book.models import Book
from bootstrap_datepicker_plus import DatePickerInput

# from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.get_free_books())

    class Meta:
        model = Order
        fields = ('user', 'book')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save order'))


class OrderFormEdit(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'end_at', 'plated_end_at')
        widgets = {
            'end_at': DatePickerInput(format='%Y-%m-%d'),
            'plated_end_at': DatePickerInput(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save order'))
