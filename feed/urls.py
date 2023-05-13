from django.urls import path
from feed.views import MainLogoutView
from .import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("logout/", MainLogoutView.as_view(), name="logout"),
    path("settings/", views.usettings, name="settings"),
]