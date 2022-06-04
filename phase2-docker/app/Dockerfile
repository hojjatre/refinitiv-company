FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install django djangorestframework numpy pandas 

CMD python manage.py makemigrations --noinput && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
