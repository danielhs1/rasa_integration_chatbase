FROM python:3.8-slim-buster

WORKDIR /srv

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    jq \
    tzdata \
    git \
    make \
    gcc \
    g++ \
    ca-certificates \
    locales locales-all \
    wget && \
    update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt_br
ENV LC_ALL pt_BR.UTF-8

# ADD APP
ADD Pipfile* ./

# INSTALL FROM REQUIREMENTS FILE
RUN pip install --no-cache -U pip pipenv && pipenv install --system --verbose

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

RUN apt-get remove --purge -y \
    gcc \
    g++ \
    wget && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y

ADD . .

ENTRYPOINT ["supervisord"]
