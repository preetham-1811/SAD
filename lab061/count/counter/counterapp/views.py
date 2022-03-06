from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Counter


def get_counter():
    try:
        counter = Counter.objects.get(name="counter")
    except:
        counter = Counter(name="counter", value=0)
        counter.save()
    return counter

def index(request):
    counter = get_counter()
    return JsonResponse({"name": counter.name, "value": counter.value})

def count(request):
    counter = get_counter()
    counter.value += 1
    counter.save()
    return JsonResponse({"result": 1})

def reset(request):
    counter = get_counter()
    counter.value = 0
    counter.save()
    return JsonResponse({"result": "Value of counter resetted to 0"})
