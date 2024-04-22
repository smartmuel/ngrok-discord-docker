# Base image for the container
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/ngrok-discord.py"]
