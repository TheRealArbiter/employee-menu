__DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres'
)



__OWN_APPS = (
    'employee_menu_service.apps.apidoc',
    'employee_menu_service.apps.menu',
    'employee_menu_service.apps.meals',
    'employee_menu_service.apps.employee',
)

__THIRD_PARTY_APPS = (
    'rest_framework',
    'django_filters',
    # 'mailer',
    # 'ordered_model',
    # 'solo',
    # 'import_export',
    # 'colorfield',
    'drf_yasg',
    'corsheaders',
    # 'ckeditor',
)


INSTALLED_APPS =  __DJANGO_APPS  + __OWN_APPS + __THIRD_PARTY_APPS
