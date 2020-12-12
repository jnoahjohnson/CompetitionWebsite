from django.urls import path
from .views import login_view, logout_view, profile_view, create_profile

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("createprofile/", create_profile, name="create_profile"),
    path("", login_view, name="login"),
]
