from django.apps import AppConfig


class MiembrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miembros'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa