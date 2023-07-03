<<<<<<< HEAD
<<<<<<< HEAD
=======
# This file shows the URLs starting in .../polls/

>>>>>>> new-things
=======
# This file shows the URLs starting in .../polls/

>>>>>>> new-things
from django.urls import path

from . import views

<<<<<<< HEAD
<<<<<<< HEAD
urlpatterns = [
    path("", views.index, name="index"),
=======
=======
>>>>>>> new-things
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),	                             # polls/
    path("<int:question_id>/", views.detail, name="detail"),             # polls/5/
    path("<int:question_id>/results/", views.results, name="results"),   # polls/5/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),            # polls/5/vote/
<<<<<<< HEAD
>>>>>>> new-things
=======
>>>>>>> new-things
]
