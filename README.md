# Patrol System

Patrol System - это веб-приложение, созданное на базе Django, предназначенное для сбора основных сведений об операционной системе и центральном процессоре удаленных хостов с использованием SSH.

## Установка и запуск приложения

1. Установить необходимые зависимости:

    ```bash
    pip install django
    pip install paramiko
    ```

2. Применить миграции:

    ```bash
    python manage.py migrate
    ```

3. Запустить сервер:

    ```bash
    python manage.py runserver
    ```

4. Открыть приложение в браузере по адресу [http://localhost:8000/patrol](http://localhost:8000/patrol)

## Использование

1. На главной странице необходимо ввести данные для подключения по SSH к удаленному хосту и нажать кнопку "Подключиться".

2. Это выполнит SSH-подключение к указанному хосту и соберет основные сведения об операционной системе и центральном процессоре.

## Конфигурация SSH

Убедитесь, что на удаленном хосте настроено подключение по SSH. Подключение выполняется по паролю.

