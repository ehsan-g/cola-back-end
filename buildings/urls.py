from django.urls import path

from django.views.generic import TemplateView

name = "buildings"
# For static render: (Only for Reference)
urlpatterns = [
    path("static", TemplateView.as_view(template_name="index.html")),
]