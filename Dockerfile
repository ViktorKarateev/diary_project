# syntax=docker/dockerfile:1

# 1. Базовый этап — установка Poetry и зависимостей
FROM python:3.13-slim AS builder

ENV POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Установим Poetry
RUN apt-get update && apt-get install -y curl build-essential libpq-dev \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && apt-get purge -y curl \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

ENV PATH="${POETRY_HOME}/bin:$PATH"

WORKDIR /app

# Скопировать pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Установим зависимости
RUN poetry install --no-root --only main

# 2. Финальный образ
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Скопируем виртуальное окружение и проект
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/include /usr/local/include
COPY --from=builder /opt/poetry /opt/poetry
COPY --from=builder /app /app

ENV PATH="/opt/poetry/bin:$PATH"

# Копируем проект
COPY . .

# Открываем порт
EXPOSE 8000

# Стартовая команда
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
