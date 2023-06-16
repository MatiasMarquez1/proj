from django.shortcuts import render
from django.http import HttpResponse

# This is the simplest possible view in django
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
