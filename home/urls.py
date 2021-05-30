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

] 