from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'app.core'

    def ready(self):
        from django.db.models.signals import pre_save
        from .signals import create_slug

        pre_save.connect(create_slug, dispatch_uid='slug.generation')
