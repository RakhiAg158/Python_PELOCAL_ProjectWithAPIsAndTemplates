from django.apps import AppConfig
from .db import initialize_db

class TodoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo_app"

    def ready(self):
        initialize_db()
