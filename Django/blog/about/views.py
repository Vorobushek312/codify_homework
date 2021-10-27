from django.shortcuts import render
from about.forms import AboutForm
from about.models import About

# Create your views here.
def about(request):
    if request.method == "POST":
        data = request.POST
        data_form = AboutForm(data=data)
        if data_form.is_valid():
            email = data_form.cleaned_data['email']
            first_name = data_form.cleaned_data['first_name']
            last_name = data_form.cleaned_data['last_name']
            message = data_form.cleaned_data['message']
            allow_mailing = data_form.cleaned_data['allow_mailing']
            about_object = About(email=email, first_name=first_name, last_name=last_name, message=message, allow_mailing=allow_mailing)
            about_object.save()
            print('Saved')

    form = AboutForm()
    about_data = About.objects.all()
    return render(request, 'project_1_index.html', {"form" : form, "data": about_data})
