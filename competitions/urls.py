from django.urls import path
from .views import competition_home_view, createCompetitions, editCompetitions, viewCompetitions, deleteCompetition

urlpatterns = [
    path("create/", createCompetitions, name="create_competition"),
    path("edit/<int:competition_id>", editCompetitions, name="edit_competition"),
    path("view/<int:competition_id>", viewCompetitions, name="competition_view"),
    path("delete/<int:competition_id>",
         deleteCompetition, name="delete_competition"),
    path("", competition_home_view, name="competition_home"),
]
