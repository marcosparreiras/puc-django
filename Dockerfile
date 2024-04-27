FROM python:3.12.3-alpine3.19

WORKDIR /usr/src/app
 
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --upgrade pip 

RUN wget -O /usr/local/bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/master/wait-for && \
    chmod +x /usr/local/bin/wait-for

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD wait-for school_db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000 --noreload
