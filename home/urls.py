from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path('signup/', views.signup, name="signup"),
]