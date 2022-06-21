from django.urls import path
from django.views.generic import TemplateView

app_name = "buildings"
# For static render: (Only for Reference)4
urlpatterns = [
    path("static", TemplateView.as_view(template_name="index.html")),
]
