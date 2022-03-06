from django.urls import path
from . import views
from rest_framework import routers

app_name = 'menu'

router = routers.SimpleRouter()
router.register(r'menu', views.MenuViewSet)


urlpatterns = [
]

urlpatterns = router.urls + urlpatterns
