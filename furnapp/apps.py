from django.apps import AppConfig


class FurnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'furnapp'

    def ready(self):
        import furnapp.signal


class TranslateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'translate'