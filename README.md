# 📘 Diary Project — API для ведения личного дневника

Приложение позволяет пользователям вести записи в личном дневнике с возможностью анализа настроения и тегирования. Реализована авторизация, API, защита прав, тестирование, контейнеризация и документация.

## 🚀 Функциональность

- JWT-аутентификация пользователей
- CRUD для записей (`Entry`)
- CRUD для настроений (`Mood`)
- CRUD для тегов (`Tag`)
- Подписка на теги (можно создавать записи только по своим тегам)
- Swagger-документация
- Тесты (coverage > 90%)
- Docker-сборка и PostgreSQL
- CI/CD пайплайн через GitHub Actions (по желанию)

## 🛠️ Стек технологий

- Python 3.13 + Poetry
- Django 5.2.5, DRF 3.16.1
- PostgreSQL
- Docker, Docker Compose
- Celery + Redis (если используется)
- GitHub Actions (опционально)
- pytest, coverage
- Swagger (drf-yasg)

## 📂 Запуск проекта

### 🔧 Клонирование

```bash
git clone https://github.com/<your_username>/diary_project.git
cd diary_project
```

### 🐳 Запуск через Docker

```bash
docker-compose up --build
```

### ⚙️ Применение миграций и создание суперпользователя

```bash
docker-compose exec web poetry run python manage.py migrate
docker-compose exec web poetry run python manage.py createsuperuser
```

## ✅ Тесты и покрытие

```bash
poetry run pytest --cov=diary
```

> Покрытие: **94%**

## 🔐 Авторизация

JWT-токены:

- `POST /api/token/` — получить токен
- `POST /api/token/refresh/` — обновить токен

## 📑 Документация

Swagger доступен по адресу:  
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## 👤 Автор

- GitHub: [@karat](https://github.com/karateev92)
- Email: karateev.92@gmail.com