from django.urls import path, include
from . import views
from .views import profile_view, user_profile

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.user_login, name="login"),
    path("notes", include('usernotes.urls')),
    path("profile", views.profile_view, name="profile"),
    path("logged_out/", views.log_out, name="log_out"),
    path('', include("django.contrib.auth.urls")),
]