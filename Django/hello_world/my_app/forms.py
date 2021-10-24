from django import forms

class AboutForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200)
    allow_mailing = forms.BooleanField()