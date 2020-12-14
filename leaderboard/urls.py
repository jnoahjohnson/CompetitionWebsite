from django.urls import path
from .views import homeLeaderboardView, editLeaderboardView, viewLeaderboardView

urlpatterns = [
    path("edit/", editLeaderboardView, name="edit"),
    path("view/", viewLeaderboardView, name="leaderboard_view"),
    path("", homeLeaderboardView, name="leaderboard_home"),
]
