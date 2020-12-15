from django.urls import path
from .views import view_leaderboard

urlpatterns = [
    path("<int:competition_id>", view_leaderboard, name="leaderboard"),
]
