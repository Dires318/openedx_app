"""
openedx_app Django admin registration.
"""
from django.contrib import admin
from .models import Greating, Test

admin.site.register(Greating)
admin.site.register(Test)