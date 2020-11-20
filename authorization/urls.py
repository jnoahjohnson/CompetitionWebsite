from django.urls import path
from .views import LoginPageView, LogoutPageView, ProfilePageView

urlpatterns = [
    path("", LoginPageView, name="login"),
    path("logout/", LogoutPageView, name="logout"),
    path("profile/", ProfilePageView, name="profile") 
]   