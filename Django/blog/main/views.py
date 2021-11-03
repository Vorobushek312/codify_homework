from django.shortcuts import render
from create.models import Create

# Create your views here.
def main(request):
    articles = Create.objects.all()
    return render(request, 'index.html', {'articles': articles})