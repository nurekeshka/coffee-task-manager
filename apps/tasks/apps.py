''' Application configuration module '''
from django.apps import AppConfig


class TasksConfig(AppConfig):
    ''' Application configuration class '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tasks'
