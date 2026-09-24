FROM python:3.14-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock README.md ./

COPY src ./src

RUN uv sync --frozen

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["sh", "-c", "uv run uvicorn ci_cd_ai_service.main:app --host 0.0.0.0 --port ${PORT:-8000}"]