FROM ghcr.io/astral-sh/uv:python3.11-trixie-slim
RUN \
  groupadd --gid 1000 app && \
  useradd \
    --no-log-init \
    --create-home \
    --shell /bin/bash \
    --uid 1000 \
    --gid 1000 \
    app
RUN apt-get update && apt-get install -y --no-install-recommends \
  cmake \
  build-essential \
  && rm -rf /var/lib/apt/lists/*
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Install libraries
WORKDIR /opt/app
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked --no-install-project
ENV PATH="/opt/app/.venv/bin:$PATH"
# Install application source code
COPY README.md ./
COPY src src/
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked
USER 1000:1000
WORKDIR /home/app
ENTRYPOINT ["qiskit-examples"]
CMD []
