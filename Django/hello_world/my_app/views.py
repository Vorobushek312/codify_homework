from django.shortcuts import render
from datetime import date, datetime
from my_app.forms import AboutForm
from my_app.models import About



# Create your views here.
def index(request):
    return render(request, 'index.html')

def current_time(request):
    time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S%z")
    date = {'time': time}
    return render(request, 'html-css-1-1.html', context = date)

def math_operation(request):
    answer = 99 + 32 - 17 / 55
    data = {'answer': answer}
    return render(request, 'html-css-1-2.html', context = data)

def my_python_tutorial(request):
    return render(request, 'html-css-2-1.html')

def my_python_tutorial_logo(request):
    return render(request, 'html-css-2-2.html')

def type_h(request):
    return render(request, 'html-css-2-3.html')
    
def css_style_wiev(request):
    return render(request, 'html-css-2-4.html')

def css_colorlib_contact_form(request):
    return render(request, 'colorlib-contact-form.html')

def cat_blog(request):
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

def template1(request):
    return render(request, 'colorlib.html')

def template2(request):
    return render(request, 'get_in_touch.html')

def template3(request):
    return render(request, 'template3.html')

def template4(request):
    return render(request, 'contact-form.html')