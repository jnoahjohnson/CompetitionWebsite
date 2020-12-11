from django.urls import path
from .views import indexPageView, editConnectFriendsView, createConnectFriendsView, joinConnectFriendsView

urlpatterns = [
    path("edit/", editConnectFriendsView, name="edit"),
    path("create/", createConnectFriendsView, name="create_group"),
    path("join/", joinConnectFriendsView, name="join"),
    path("", indexPageView, name="connectfriends_home")
]
