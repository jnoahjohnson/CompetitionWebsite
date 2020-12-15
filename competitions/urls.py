from django.urls import path
from .views import competition_home_view, createCompetitions, editCompetitions, viewCompetitions, deleteCompetition, task_completed, competition_about

urlpatterns = [
    path("create/", createCompetitions, name="create_competition"),
    path("edit/<int:competition_id>", editCompetitions, name="edit_competition"),
    path("view/<int:competition_id>", viewCompetitions, name="competition_view"),
    path("delete/<int:competition_id>",
         deleteCompetition, name="delete_competition"),
    path("taskcompeted/<int:competition_id>",
         task_completed, name="task_completed"),
    path("competitions", competition_home_view, name="competition_home"),
    path("", competition_about, name="competition_about"),
]
