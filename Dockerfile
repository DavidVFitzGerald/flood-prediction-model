FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" "./"

RUN uv sync --locked

COPY "predict.py" "model.bin" "./"

EXPOSE 8000

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]