FROM python:3.12-slim

WORKDIR /messengerbot-api

COPY . .

RUN apt update && \
    apt-get install git build-essential libffi-dev libssl-dev openssl --no-install-recommends -y \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 4371

CMD [ "python3", "-m" , "sanic", "app:app", "--fast", "--access-logs", "--motd", "--noisy-exceptions", "-H", "0.0.0.0"]