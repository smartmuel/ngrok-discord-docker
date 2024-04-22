FROM python:3.12.1-slim-bookworm

WORKDIR /app

COPY requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/ngrok-discord.py"]
