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

def CLP(request):
    return render(request, 'CLP.html')

def PLUE(request):
    return render(request, 'PLUE.html')

def TLUE(request):
    return render(request, 'TLUE.html')

def recipro_oilfreetype(request):
    return render(request, 'recipro_oilfreetype.html')

def TFP(request):
    return render(request, 'TFP.html')

def CFP(request):
    return render(request, 'CFP.html')

def OFP(request):
    return render(request, 'OFP.html')

def PFUE(request):
    return render(request, 'PFUE.html')

def CFUE(request):
    return render(request, 'CFUE.html')