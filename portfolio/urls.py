from django.urls import path
from . import views

urlpatterns = [
    path("", views.starter_page, name="starter_page"),
    path("home/", views.index, name="home"),
    path("project-details/", views.project_details, name="portfolio_details"),
]