ARG ARCH=amd64  # Default architecture
ARG PYTHON_VERSION=3.12

FROM --platform=${ARCH} python:${PYTHON_VERSION}-${ARCH}-slim  # Use base image based on build argument


WORKDIR /app

COPY requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/ngrok-discord.py"]
