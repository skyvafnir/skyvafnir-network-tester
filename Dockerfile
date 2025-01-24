FROM python:3.11-slim-buster AS builder

RUN pip install poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR


FROM python:3.11-slim-buster AS runtime


WORKDIR /app
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY skyvafnir_network_test ./skyvafnir_network_test

ARG GIT_SHA
ARG VERSION

ENV GIT_SHA ${GIT_SHA}
ENV VERSION ${VERSION}

LABEL is.skyvafnir.tags.service="skyvafnir-network-test"
LABEL is.skyvafnir.tags.version="${VERSION}"
LABEL is.skyvafnir.tags.sha="${GIT_SHA}"

CMD ["uvicorn", "skyvafnir_network_test.main:app", "--host", "0.0.0.0", "--port", "8000"]
