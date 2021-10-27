from django import forms
from create.models import Create

class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        exclude = ('create_date', 'update_date')
