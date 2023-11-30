"""
URLs for openedx_app.
"""
from django.urls import re_path, path
from django.views.generic import TemplateView
from .views import GreatingDetail, GreatingList
urlpatterns = [
    path('greating/', GreatingList.as_view(), name="Greating List"),
    path("greating/<int:pk>/", GreatingDetail.as_view(), name="greating_detail"),
    # re_path(r'', TemplateView.as_view(template_name="openedx_app/base.html")),
]
