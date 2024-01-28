from django.urls import path, include
from . import views
from .views import user_profile

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.user_login, name="login"),
    path("notes/", views.notes, name="notes"),
    #path("profile/", user_profile, name="profile"),
    path('<str:username>', user_profile, name='profile'),
    path("logged_out/", views.log_out, name="log_out"),
    path("profile/login/", views.user_login),
    path("create_note/", views.create_note, name="create_note"),

]
urlpatterns += [
    path('profile/', include('django.contrib.auth.urls')),
]
