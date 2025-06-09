# backend/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Cài đặt các dependency
COPY Legendary/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy toàn bộ code vào container
COPY Legendary/ .

# Chạy các lệnh migrate khi container khởi động
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 legend.asgi:application"]