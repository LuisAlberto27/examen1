"""examen1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from inicio.views import vista_Inicio, form_Asistente, form_Ponente, form_Staff

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', vista_Inicio.as_view(), name='index_view'),
    #url(r'^NuevoAsistentes/$', vista_Asistente.as_view(), name='asistente_view'),
    #url(r'^NuevoPonentes$', vista_Ponente.as_view(), name='about_view'),
    #url(r'^NuevoStaff$', vista_Staff.as_view(), name='contact_view'),
    #urls a los formularios.
    url(r'RegistroAsistente$', form_Asistente.as_view(),name='form_Asistente_view'),
    url(r'RegistroPonente$', form_Asistente.as_view(),name='form_Ponente_view'),
    url(r'RegistroStaff$', form_Asistente.as_view(),name='form_Staff_view'),
    url(r'^Asistentes$','inicio.views.asistente', name='todos_asistentes'),
    url(r'^Ponentes$','inicio.views.ponente', name='todos_ponentes'),
    url(r'^Staff$','inicio.views.staff',name='todos_staff'),


]
