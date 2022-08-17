FROM python:3.9 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9
WORKDIR /skyvafnir-network-test
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY skyvafnir_network_test ./skyvafnir_network_test

ARG GIT_SHA
ARG VERSION

ENV GIT_SHA ${GIT_SHA}
ENV VERSION ${VERSION}

LABEL is.skyvafnir.tags.service="skyvafnir-network-test"
LABEL is.skyvafnir.tags.version="${VERSION}"
LABEL is.skyvafnir.tags.sha="${GIT_SHA}"

CMD ["uvicorn", "skyvafnir_network_test.main:app", "--host", "0.0.0.0", "--port", "8000"]
