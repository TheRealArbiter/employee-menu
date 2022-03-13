from django.db import models
from django.utils.translation import gettext as _
from employee_menu_service.apps.functions import get_clean_uuid
MAIN_APP_PATH = 'meals/'

# Create your models here.
class Meals(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=get_clean_uuid, editable=False)
    name = models.CharField(max_length=150, verbose_name=_("Nombre de la comida"))