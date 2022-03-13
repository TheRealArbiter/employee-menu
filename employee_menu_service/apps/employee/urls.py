from django.urls import path
from . import views
from rest_framework import routers

app_name = 'employee'

router = routers.SimpleRouter()
router.register(r'employee', views.EmployeeViewSet)


urlpatterns = [
]

urlpatterns = router.urls + urlpatterns