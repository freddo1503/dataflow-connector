FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app

COPY ./pyproject.toml /app/
COPY ./uv.lock /app/

RUN uv sync

COPY . /app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000"]
