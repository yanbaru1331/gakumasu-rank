FROM python:3.12.3

ENV PATH="/root/.local/bin:$PATH" 
ENV POETRY_HOME=/opt/poetry
WORKDIR /Gakumasu


RUN wget -O - https://install.python-poetry.org | python3 - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && apt update
