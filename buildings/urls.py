from django.urls import path

from django.views.generic import TemplateView

name = "buildings"

urlpatterns = [
    path("", TemplateView.as_view(template_name="templates/index.html")),
]