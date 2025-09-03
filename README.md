# 📘 Diary API — Личный дневник  

REST API-сервис для ведения личных записей, отслеживания настроения и подписок на интересующие теги.  
Позволяет создавать записи только по подписанным тегам, фильтровать их по тегам и дате, авторизоваться через JWT и использовать систему подписок.  

## 🚀 Стек технологий  
- Python 3.11+  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- drf-yasg (Swagger)  
- Docker + Docker Compose  
- JWT (SimpleJWT)  
- Pytest + Coverage  

## ⚙️ Установка и запуск  
1. Клонируйте проект:  
   git clone https://github.com/ViktorKarateev/diary_project.git  
   cd diary_project  
2. Создайте файл `.env` на основе `.env.example`.  
3. Запустите проект в Docker:  
   docker-compose up --build  
4. Примените миграции:  
   docker-compose exec web python manage.py migrate  
5. Создайте суперпользователя:  
   docker-compose exec web python manage.py createsuperuser  

## 🔐 Авторизация (JWT)  
Получение токена:  
POST /api/token/  
{ "email": "your_email@example.com", "password": "your_password" }  

Обновление токена:  
POST /api/token/refresh/  
{ "refresh": "your_refresh_token" }  

Использование:  
Authorization: Bearer <access_token>  

## 🔄 Основные эндпоинты  
- GET /api/entries/ — список записей (только владелец)  
- POST /api/entries/ — создать запись (по подписанным тегам)  
- GET /api/moods/ — список настроений  
- POST /api/tags/subscribe/ — подписка на теги  
- GET /swagger/ — Swagger-документация  
- GET /api/entries/?search=слово — поиск по API  
- GET /entries/?q=слово — поиск в HTML-интерфейсе  

## 🌐 Переменные окружения (.env.example)  
DEBUG=True  
SECRET_KEY=your_secret_key  
POSTGRES_DB=diary_db  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=your_password  
POSTGRES_HOST=db  
POSTGRES_PORT=5432  
ALLOWED_HOSTS=127.0.0.1,localhost  

## 📄 Документация  
Swagger доступен по адресу:  
http://localhost:8000/swagger/  

## 🧪 Тесты  
Тесты реализованы с использованием pytest и coverage.  

Запуск тестов:  
pytest --cov  

Покрытие: 94%  

## 📈 Бизнес-ценность проекта  
Проект позволяет пользователям:  
- Отслеживать своё психоэмоциональное состояние (через модель настроений)  
- Фокусироваться на интересующих темах (подписки на теги)  
- Экономить время благодаря фильтрации записей  

Пример:  
Пользователь тратит ~15 минут в день на рефлексию.  
Благодаря фильтрам экономится до 30% времени.  
Это ~7 часов в месяц + повышение вовлечённости.  

## 📌 Автор  
Виктор Каратеев — 2025  

GitHub: https://github.com/ViktorKarateev/diary_project  
