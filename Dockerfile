FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency file first for caching
COPY pyproject.toml ./

# Install dependencies (this works only if pyproject.toml is valid as above)
RUN uv pip install --system --no-cache-dir .

# Copy everything else
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
