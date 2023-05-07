from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path('signup/', views.signup, name="signup"),
    path('signup/generatepass/', views.generate_confcode, name="generate_confcode"),
    path('signup/verify/', views.check_code, name="check_code"),
    path('login/', views.login, name="login"),
]