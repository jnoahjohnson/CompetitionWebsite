from django.urls import path
from .views import indexPageView, Login, Logout

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),   
]   