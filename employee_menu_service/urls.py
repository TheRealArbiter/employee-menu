from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .starter import Starter
from employee_menu_service.apps.apidoc.config import schema_view

urlpatterns = [
    path('', Starter.as_view(), name="starter"),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # API configuration.
    path('api/doc/(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Own Django Apps.
    # path('person/', include('people.apps.person.urls')),
    # path('setup/', include('people.apps.setup.urls')),
    # path('business/', include('people.apps.business.urls')),
    # path('noticenter/', include('people.apps.noticenter.urls')),
    # path('payroll/', include('people.apps.payroll.urls')),
    # path('intranet/', include('people.apps.intranet.urls')),
    # path('fiscal/', include('people.apps.fiscal.urls')),
]

if settings.DEBUG:  # Adding statics only if debug = True
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)