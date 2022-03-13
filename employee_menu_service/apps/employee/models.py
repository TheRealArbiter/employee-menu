from django.db import models
from django.utils.translation import gettext as _
from employee_menu_service.apps.functions import get_clean_uuid
MAIN_APP_PATH = 'employee/'

# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=get_clean_uuid, editable=False)
    name = models.CharField(max_length=150, verbose_name=_("Nombre del empleado"))
    email = models.CharField(max_length=30, verbose_name=_("Correo del empleado"))
    phone = models.IntegerField(max_length=12, verbose_name=_("Número del empleado"))