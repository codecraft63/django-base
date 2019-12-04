from django.apps import AppConfig
from django.db.models.signals import pre_save


class DefaultConfig(AppConfig):
    name = 'app.core'
    label = 'core'
    verbose_name = "App Core"

    def ready(self):
        from .signals import create_slug

        pre_save.connect(create_slug, dispatch_uid='slug.generation')
