from django.urls import path
from feed.views import MainLogoutView
from .import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path('myguilds/', views.myguilds, name='myguilds'),
    path("logout/", MainLogoutView.as_view(), name="logout"),
    path("settings/", views.usettings, name="settings"),
    path("settings/changepassword/", views.usettings_changepass, name="usettings_changepass"),
    path('settings/upload/', views.upload_photo, name='upload_photo'),
]