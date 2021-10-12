from django.shortcuts import render
from test_form.forms import MyForms

# Create your views here.
def form_url(request):
    form = MyForms
    return render(request, 'test-form.html', {'form' : form})