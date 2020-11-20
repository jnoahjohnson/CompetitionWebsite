from django.urls import path
from .views import indexPageView, createCompetitions, editCompetitions, viewCompetitions

urlpatterns = [
    path("", indexPageView, name="index"),
    path("create/", createCompetitions, name="create"),
    path("edit/", editCompetitions, name="edit"),
    path("view/", viewCompetitions, name="view"),
]
