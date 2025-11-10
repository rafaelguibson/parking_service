from django.apps import AppConfig


class ParkingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parking'
    verbose_name = 'ID da Vaga'
    verbose_name_plural = 'IDs das Vagas'
