from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("login/", views.login_view, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("logout/", views.logout_view, name="logout"),

    path("register/", views.register_view, name="register"),

    path("basic-test/", views.basic_test, name="basic_test"),

    path(
        "communication/",
        views.communication_assessment,
        name="communication_assessment"
    ),

    path(
        "team-discussion/",
        views.team_discussion,
        name="team_discussion"
    ),

    path(
        "technical-assessment/",
        views.technical_assessment,
        name="technical_assessment"
    ),

    path(
        "interview-readiness/",
        views.interview_readiness,
        name="interview_readiness"
    ),

    path(
    "final-result/",
    views.final_result,
    name="final_result"
),
]