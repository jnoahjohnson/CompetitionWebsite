from django.urls import path
from .views import indexPageView, createCompetitions, editCompetitions, viewCompetitions

urlpatterns = [
    path("create/", createCompetitions, name="create_competition"),
    path("edit/<int:competition_id>", editCompetitions, name="edit_competition"),
    path("view/<int:competition_id>", viewCompetitions, name="competition_view"),
    path("", indexPageView, name="index"),
]
