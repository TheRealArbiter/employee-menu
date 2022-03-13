from django.urls import path
from . import views
from rest_framework import routers

app_name = 'meals'

router = routers.SimpleRouter()
router.register(r'meals', views.MenuViewSet)


urlpatterns = [
]

urlpatterns = router.urls + urlpatterns
