from django.shortcuts import render
from create.forms import CreateForm
# Create your views here.
def create(request):
    if request.method == 'POST':
        article_form = CreateForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
        else:
            return render(request, 'create-article.html', {"form" : article_form, "errors" : article_form.errors})

    form = CreateForm()
    return render(request, 'create-article.html', {"form": form})