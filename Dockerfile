FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip \
    && unzip allure-2.13.8.zip -d /opt/ \
    && rm allure-2.13.8.zip \
    && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV OPENCART_HOST=http://opencart:8080
ENV OPENCART_DATABASE_HOST=mariadb
ENV OPENCART_DATABASE_PORT=3306
ENV OPENCART_DATABASE_USER=bn_opencart
ENV OPENCART_DATABASE_NAME=bitnami_opencart
ENV SELENOID_URL=http://selenoid:4444/wd/hub
ENV BROWSER=chrome
ENV BROWSER_VERSION=latest
ENV THREADS=1

CMD ["pytest", "--alluredir=/app/allure-results", "--url=http://opencart:8080", "--browser=chrome", "--browser_version=latest", "--threads=1", "--selenoid=http://selenoid:4444/wd/hub"]