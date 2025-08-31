# 📘 Diary API — Личный дневник  
REST API-сервис для ведения личных записей, отслеживания настроения и подписок на интересующие теги. Позволяет создавать записи только по подписанным тегам, фильтровать по тегам и дате, авторизоваться через JWT и использовать систему подписок.  
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
git clone https://github.com/yourusername/diary_project.git  
cd diary_project  
2. Создайте `.env` на основе `.env.example`.  
3. Запустите в Docker:  
docker-compose up --build  
4. Примените миграции:  
docker-compose exec web python manage.py migrate  
5. Создайте суперпользователя:  
docker-compose exec web python manage.py createsuperuser  
## 🔐 Авторизация (JWT)  
Для получения токена:  
POST /api/token/  
{ "email": "your_email@example.com", "password": "your_password" }  
Для обновления:  
POST /api/token/refresh/  
{ "refresh": "your_refresh_token" }  
Добавляйте access-токен в заголовок:  
Authorization: Bearer <access_token>  
## 🔄 Основные эндпоинты  
GET /api/entries/ — список записей (доступно только владельцу)  
POST /api/entries/ — создать запись (по подписанным тегам)  
GET /api/moods/ — список настроений  
POST /api/tags/subscribe/ — подписка на теги  
GET /swagger/ — Swagger-документация  
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
Документация Swagger доступна по адресу:  
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
- Экономить время — автоматизация и фильтрация записей (по дате, тегу)  
Пример оценки:  
Пользователь тратит ~15 минут в день на рефлексию и анализ.  
Благодаря фильтру по настроениям и тегам — 30% времени экономится.  
7 часов в месяц — высвобожденное время, +повышение вовлечённости.  
## 📌 Автор  
Виктор Каратеев — 2025  
GitHub: https://github.com/yourusername  
