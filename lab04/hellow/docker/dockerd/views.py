from django.shortcuts import render

# Create your views here.
def dockerd(request):
    return render(request, 'dockerd.html', {})
