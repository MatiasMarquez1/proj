# This file shows the URLs starting in .../polls/

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),	# polls/
]
