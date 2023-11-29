"""
URLs for openedx_app.
"""
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    re_path(r'', TemplateView.as_view(template_name="openedx_app/base.html")),
]
