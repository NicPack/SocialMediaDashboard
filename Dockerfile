FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files for better caching
COPY pyproject.toml ./

# Install dependencies including Streamlit
RUN uv pip install --system --no-cache-dir \
    streamlit \
    && uv pip install --system --no-cache-dir -e .

# Copy the rest of the application
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]