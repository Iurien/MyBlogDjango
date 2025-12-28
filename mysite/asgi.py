"""
Конфигурация ASGI для проекта mysite.

Она предоставляет доступ к вызываемой функции ASGI в виде переменной уровня модуля с именем ``application``.

Дополнительную информацию об этом файле см. в разделе
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
