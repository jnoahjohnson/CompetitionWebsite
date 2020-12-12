from django.urls import path
from .views import indexPageView, editLeaderboardView, viewLeaderboardView

urlpatterns = [
    path("edit/", editLeaderboardView, name="edit"),
    path("view/", viewLeaderboardView, name="leaderboard_view"),
    path("", indexPageView, name="leaderboard_index"),
]
