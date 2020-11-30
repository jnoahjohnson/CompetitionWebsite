from django.urls import path
from .views import indexPageView, editConnectFriendsView, createConnectFriendsView, joinConnectFriendsView

urlpatterns = [
    path("edit/", editConnectFriendsView, name="edit_group"),
    path("create/", createConnectFriendsView, name="create_group"),
    path("join/", joinConnectFriendsView, name="join_group"),
    path("", indexPageView, name="connectfriends_home")
] 