FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y wget unzip curl firefox-esr && \
    apt-get clean

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

RUN apt-get install -y xvfb

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]

CMD ["--browser=firefox"]
