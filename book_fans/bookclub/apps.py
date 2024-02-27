from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookclubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookclub'


    class Meta:
        verbose_name = _('bookclub')
