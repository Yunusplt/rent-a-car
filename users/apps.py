from django.apps import AppConfig
#!0708 signal olusturduktan sonra buraya geldik. signali import et. 

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals