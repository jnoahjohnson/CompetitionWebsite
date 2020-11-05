from django.urls import path
from .views import indexPageView, editConnectFriendsView, createConnectFriendsView, joinConnectFriendsView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("edit/", editConnectFriendsView, name="edit"),
    path("create/", createConnectFriendsView, name="create"),
    path("join/", joinConnectFriendsView, name="join")
] 