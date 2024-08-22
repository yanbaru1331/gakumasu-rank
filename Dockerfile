FROM python:3.12.3

ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_HOME=/opt/poetry
WORKDIR /Gakumasu

# 必要なパッケージをインストール
#RUN apt-get update && apt-get install -y wget curl
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    apt-get clean

#RUN curl -sSL https://install.python-poetry.org/ | python -

# Cargoのインストール
#RUN curl https://sh.rustup.rs -sSf | sh
#RUN ENV PATH="/root/.cargo/bin:$PATH"
#
# Poetryのインストール
#RUN wget -O - https://install.python-poetry.org | python3 - --no-check-certificate

# Poetryの設定
#RUN ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry \
#    && poetry config virtualenvs.create false \
#    && apt-get update

#ENV PATH /root/.local/bin
