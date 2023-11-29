"""
openedx_app Django application initialization.
"""

import logging

from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs

log = logging.getLogger(__name__)


class OpenedxAppConfig(AppConfig):
    """
    Configuration for the openedx_app Django application.
    """

    name = 'openedx_app'
    verbose_name = "My Open edX Plugin"

    # See: https://edx.readthedocs.io/projects/edx-django-utils/en/latest/edx_django_utils.plugins.html
    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^openedx_app/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                "production": {PluginSettings.RELATIVE_PATH: "settings.production"},
                "common": {PluginSettings.RELATIVE_PATH: "settings.common"},
            }
        },
    }

    def ready(self):
        """
        Make ready for debug of the openedx_app.
        """
        log.debug("%s is ready.", self.label)
