from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("compressor", views.compressor, name='compressor'),
    path("recipro_oillubricatedtype", views.recipro_oillubricatedtype, name='recipro_oillubricatedtype'),
    path("TLP", views.TLP, name='TLP'),
    path("CLP", views.CLP, name='CLP'),
    path("PLUE", views.PLUE, name='PLUE'),
    path("TLUE", views.TLUE, name='TLUE'),
    path("recipro_oilfreetype", views.recipro_oilfreetype, name='recipro_oilfreetype'),
    path("TFP", views.TFP, name='TFP'),
    path("CFP", views.CFP, name='CFP'),
    path("OFP", views.OFP, name='OFP'),
    path("PFUE", views.PFUE, name='PFUE'),
    path("CFUE", views.CFUE, name='CFUE'),

] 