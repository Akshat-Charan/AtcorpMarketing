from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return render(request, 'contact.html')

def compressor(request):
    return render(request, 'compressor.html')

def recipro_oillubricatedtype(request):
    return render(request, 'recipro_oillubricatedtype.html')

def TLP(request):
    return render(request, 'TLP.html')

