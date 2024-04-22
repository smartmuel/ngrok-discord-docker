ARG ARCH=amd64  # Default architecture

FROM python:${ARCH}-slim  # Use base image based on build argument

WORKDIR /app

COPY requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/ngrok-discord.py"]
