# syntax=docker/dockerfile:1

FROM python:3.13-slim

ENV POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl build-essential libpq-dev \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && apt-get purge -y curl && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

ENV PATH="${POETRY_HOME}/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --only main

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
