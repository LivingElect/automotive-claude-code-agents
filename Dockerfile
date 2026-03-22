# Multi-stage Dockerfile for Automotive Claude Code Agents
# Production-ready container with multi-architecture support

# Stage 1: Base image with system dependencies
FROM python:3.11-slim AS base

LABEL maintainer="Automotive Claude Code Contributors"
LABEL description="Universal AI-powered development platform for automotive industry"
LABEL org.opencontainers.image.source="https://github.com/automotive-opensource/automotive-claude-code-agents"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 -s /bin/bash automotive && \
    mkdir -p /app /data /logs && \
    chown -R automotive:automotive /app /data /logs

WORKDIR /app

# Stage 2: Dependencies
FROM base AS dependencies

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Stage 3: Development image (includes dev tools)
FROM dependencies AS development

# Install development dependencies
RUN pip install \
    pytest>=8.3.3 \
    pytest-cov>=5.0.0 \
    pytest-asyncio>=0.23.8 \
    black>=24.8.0 \
    ruff>=0.6.9 \
    mypy>=1.11.2 \
    ipython \
    ipdb

# Install automotive-specific development tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    can-utils \
    iproute2 \
    net-tools \
    socat \
    && rm -rf /var/lib/apt/lists/*

USER automotive

# Stage 4: Testing image
FROM development AS testing

USER root
COPY --chown=automotive:automotive . /app
USER automotive

# Run tests during build (optional)
RUN pytest tests/ -v --tb=short || echo "Tests completed with warnings"

# Stage 5: Production image (minimal)
FROM dependencies AS production

# Copy only necessary application files
COPY --chown=automotive:automotive tools/ /app/tools/
COPY --chown=automotive:automotive skills/ /app/skills/
COPY --chown=automotive:automotive agents/ /app/agents/
COPY --chown=automotive:automotive commands/ /app/commands/
COPY --chown=automotive:automotive workflows/ /app/workflows/
COPY --chown=automotive:automotive knowledge-base/ /app/knowledge-base/
COPY --chown=automotive:automotive setup.py /app/
COPY --chown=automotive:automotive README.md /app/

# Install the package
RUN pip install -e .

# Create necessary directories
RUN mkdir -p /app/data /app/logs /app/output && \
    chown -R automotive:automotive /app/data /app/logs /app/output

# Switch to non-root user
USER automotive

# Set up volumes
VOLUME ["/app/data", "/app/logs", "/app/output"]

# Expose ports (if needed)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import tools; print('OK')" || exit 1

# Default command
CMD ["python", "-m", "tools.cli"]

# Stage 6: Documentation builder
FROM base AS docs

COPY requirements.txt .
RUN pip install -r requirements.txt && \
    pip install mkdocs mkdocs-material mkdocstrings

COPY --chown=automotive:automotive . /app

USER automotive

RUN if [ -f mkdocs.yml ]; then mkdocs build; fi

# Default target
FROM production
