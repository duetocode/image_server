FROM python:3.8.11-bullseye

WORKDIR /application

VOLUME /application/data

COPY requirements.txt requirements.txt
RUN pip config set global.index-url https://mirrors.sustech.edu.cn/pypi/simple
RUN pip install -r requirements.txt 

COPY server.py database.py uwsgi.ini ./

EXPOSE 8080

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]