## Блог на Django
Блог на Django — это удобное для начинающих приложение для ведения блога. В этом проекте показаны представления на основе классов Django, как использовать модели Django с пользовательским менеджером моделей, как использовать пользовательские теги шаблонов, формы Django и формы моделей, как отправлять почту с помощью Django, как добавить синдикацию RSS,
а также как генерировать карту сайта и модульные тесты для тегов моделей, представлений, форм и шаблонов, а также как заполнять базу данных с помощью Factory Boy, Faker и команд управления.

## Начало работы
Эти инструкции помогут вам запустить копию проекта на вашем локальном компьютере для разработки и тестирования.

## Установка
```
Откройте терминал и введите
git clone https://github.com/devmahmud/DjangoBlog.git
```

#### или просто скачайте по ссылке ниже
```
https://github.com/devmahmud/DjangoBlog.git
```

## Требования
```
Создайте виртуальное окружение и активируйте его.
и установите необходимые зависимости, введя:

pip install -r requirements.txt
```

### В этом проекте я использовал PostgreSQL в качестве базы данных. Измените информацию о базе данных в настройках на информацию о вашей базе данных.
## Для миграции базы данных откройте терминал в каталоге проекта и введите:
```
python manage.py makemigrations
python manage.py migrate
```

## Сбор статических файлов
```
python manage.py collectstatic
```

## Создание суперпользователя
```
python manage.py createsuperuser
```

## Создание фиктивных данных с помощью faker
```
python manage.py seed --posts number_of_post
пример: python manage.py seed --posts 50
```

## Для отправки сообщений по электронной почте измените конфигурацию электронной почты
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ваш email'
EMAIL_HOST_PASSWORD = 'пароль вашего email'
```

## Для запуска программы на локальном сервере используйте следующую команду:
```
python manage.py runserver
Затем перейдите по адресу http://127.0.0.1:8000 в вашем браузер
```

## Для тестирования проекта
```
python manage.py test
```

## Для тестирования проекта и руководства по стилю PEP8
```
python manage.py test && flake8
```
или вы можете просто запустить `flake8`

## Снимок проекта

### Домашняя страница
![image](https://user-images.githubusercontent.com/19981097/81924503-08809680-9601-11ea-9df2-2096f265b0e1.png)

### Подробности Страница
![image](https://user-images.githubusercontent.com/19981097/81924659-37970800-9601-11ea-8433-8b21e75594b1.png)

### Страница комментариев
![image](https://user-images.githubusercontent.com/19981097/81924734-51d0e600-9601-11ea-9df9-14b9c47c11ac.png)

### Поделиться записью страница
![image](https://user-images.githubusercontent.com/19981097/81926022-2a7b1880-9603-11ea-9cd6-3f465389f250.png)

## Автор
```
Махмудул Алам
Email: expelmahmud@gmail.com
```

<div align="center">
<h3>========Спасибо!!!=========</h3>
</div>