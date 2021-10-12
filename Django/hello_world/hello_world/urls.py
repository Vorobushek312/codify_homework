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
from my_app.views import index, current_time, math_operation, my_python_tutorial, my_python_tutorial_logo, type_h, css_style_wiev
from test_form.views import form_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('html-css-1-1/', current_time, name='html-css-1-1'),
    path('html-css-1-2/', math_operation, name='html-css-1-2'),
    path('test-form/', form_url),
    path('html-css-2-1/', my_python_tutorial, name='html-css-2-1'),
    path('html-css-2-2/', my_python_tutorial_logo, name='html-css-2-2'),
    path('html-css-2-3/', type_h, name='html-css-2-3'),
    path('html-css-2-4/', css_style_wiev, name='html-css-2-4')

]