"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import index, current_time, math_operation, my_python_tutorial, my_python_tutorial_logo, type_h, css_style_wiev, css_colorlib_contact_form, cat_blog, template1, template2, template3, template4
from test_form.views import form_url
from calculator.views import get_calculator

urlpatterns = [
    path('calc/', get_calculator, name='calc'),
    path('admin/', admin.site.urls),
    path('', index),
    path('html-css-1-1/', current_time, name='html-css-1-1'),
    path('html-css-1-2/', math_operation, name='html-css-1-2'),
    path('test-form/', form_url),
    path('html-css-2-1/', my_python_tutorial, name='html-css-2-1'),
    path('html-css-2-2/', my_python_tutorial_logo, name='html-css-2-2'),
    path('html-css-2-3/', type_h, name='html-css-2-3'),
    path('html-css-2-4/', css_style_wiev, name='html-css-2-4'),
    path('colorlib-contact-form/', css_colorlib_contact_form, name='colorlib-contact-form'),
    path('cat_blog/', cat_blog, name='cat-blog'),
    path('template1/', template1, name='template1'),
    path('template2/', template2, name='template2'),
    path('template3/', template3, name='template3'),
    path('template4/', template4, name='template4')

]