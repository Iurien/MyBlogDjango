"""
Конфигурация WSGI для проекта mysite.

Она предоставляет доступ к вызываемой функции WSGI в виде переменной уровня модуля с именем ``application``.

Дополнительную информацию об этом файле см. по ссылке:
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
