FROM python:3.12-slim

FROM sanicframework/sanic:3.8-latest

WORKDIR /messengerbot-api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4371

CMD [ "python3", "-m" , "sanic", "app:app", "--fast", "--access-logs", "--motd", "--noisy-exceptions", "-H", "0.0.0.0"]