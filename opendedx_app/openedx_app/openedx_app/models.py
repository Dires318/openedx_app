"""
Database models for openedx_app.
"""
from django.db import models
from model_utils.models import TimeStampedModel


class Greating(TimeStampedModel):
    """
    Greating model response for request.

    .. no_pii:
    """

    request = models.CharField(max_length=150)
    response = models.CharField(max_length=150)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return self.request


class Test(TimeStampedModel):
    """
    This is test model for open edx.

    .. no_pii:
    """

    title = models.CharField(max_length=150)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return self.title
