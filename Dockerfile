FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /srv

# Create app/static directory and download Tachyons CSS
RUN mkdir -p app/static \
    && python -c "import urllib.request; urllib.request.urlretrieve('https://unpkg.com/tachyons@4.12.0/css/tachyons.min.css', 'app/static/tachyons.min.css')"

# Copy dependency files
COPY pyproject.toml .

# Install dependencies using uv sync (no dev dependencies)
RUN uv sync --no-dev

# Update PATH to include local bin
ENV PATH="/srv/.venv/bin:$PATH"

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run using waitress
CMD ["waitress-serve", "--host=0.0.0.0", "--port=8000", "--call", "app:create_app"] 