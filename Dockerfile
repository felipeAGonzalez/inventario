FROM python:3.9.16-alpine3.17

WORKDIR /inventario

RUN apk update \
    && apk add --no-cache gcc musl-dev mysql-dev postgresql-dev python3-dev libffi-dev git \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
