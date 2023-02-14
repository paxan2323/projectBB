FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www/html/
COPY requirements.txt /var/www/html/
RUN pip install -r requirements.txt
COPY . /var/www/html/
