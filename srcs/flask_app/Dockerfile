FROM    python:3.8

WORKDIR /opt/quiz_app

COPY    ./conf/requirements.txt /opt/quiz_app/

RUN     pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt

RUN     mkdir /opt/quiz_app/logs && \
        chmod -R 644 /opt/quiz_app

COPY    ./flask_app/web_app .

EXPOSE  5040

CMD     ["uwsgi", "--ini", "./conf/uwsgi.ini"]