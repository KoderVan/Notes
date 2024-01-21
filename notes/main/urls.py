from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.login, name="login"),
    path("notes/", views.notes, name="notes")
]
