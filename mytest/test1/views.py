from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_view(request):
    return HttpResponse("Ya, creo que aprendí a hacer apps en django")
