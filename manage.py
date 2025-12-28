#!/usr/bin/env python
"""Утилита командной строки Django для выполнения административных задач."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, "
            "что он установлен и доступен в переменной среды PYTHONPATH? "
            "Вы забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
