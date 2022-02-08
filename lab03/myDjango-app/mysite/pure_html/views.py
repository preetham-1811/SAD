from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'index.html')

def indexint(request):
    return render(request, 'indexint.html')

def indexcli(request):
    return render(request, 'indexcli.html')

def index2(request):
    return render(request, 'index2.html')