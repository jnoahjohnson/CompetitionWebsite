from django.urls import path
from .views import indexPageView, editLeaderboardView, viewLeaderboardView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("edit/", editLeaderboardView, name="edit"),
    path("view/", viewLeaderboardView, name="view") 
]     