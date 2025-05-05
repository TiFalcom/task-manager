FROM python:3.12-slim

ENV POETRY_VERSION=2.1.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar system deps + Poetry
RUN apt-get update && apt-get install -y curl build-essential libpq-dev && \
    curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION && \
    ln -s ~/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

# Copiar arquivos de dependências e instalar
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-root

# Copiar o código-fonte
COPY . .

# Expor porta e rodar app
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
