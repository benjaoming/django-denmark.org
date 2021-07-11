from django.urls import path

from . import views


app_name = "memberships"

urlpatterns = [
    path("", views.StartView.as_view(), name="start"),
    path("invite", views.InviteView.as_view(), name="invite"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("newsletter/", views.NewsletterSignupView.as_view()),
]
