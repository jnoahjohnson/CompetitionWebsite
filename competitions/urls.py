from django.urls import path
from .views import indexPageView, createCompetitions, editCompetitions, viewCompetitions

urlpatterns = [
    path("create/", createCompetitions, name="create_competition"),
    path("edit/", editCompetitions, name="edit"),
    path("view/<int:competition_id>", viewCompetitions, name="competition_view"),
    path("", indexPageView, name="index"),
]
