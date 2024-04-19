from django.apps import AppConfig


class PlantelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plantel'
    
    def ready(self):
        import plantel.signals