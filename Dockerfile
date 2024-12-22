FROM python:3.9-alpine AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=main

RUN apk add --no-cache \
    build-base \
    gcc \
    postgresql-dev \
    musl-dev \
    libffi-dev \
    libc-dev \
    binutils

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# -------------------------------------------------------------------------------------------------------------------------------- # 

FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=main

COPY --from=builder /install /usr/local

WORKDIR /app
    
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
