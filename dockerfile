FROM python:3.8.5

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD python /code/manage.py runserver 0:8000
# CMD gunicorn yatube_api.wsgi:application --bind 0.0.0.0:8000