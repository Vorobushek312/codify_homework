from django.shortcuts import render
from datetime import datetime


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