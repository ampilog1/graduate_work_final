# Dockerfile for Django
FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app/

# Копируем файл requirements.txt в /app/
COPY requirements.txt /app/

# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r requirements.txt

# Копируем все файлы и директории из текущего каталога в /app/
COPY . /app/

# Указываем точку входа для контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]