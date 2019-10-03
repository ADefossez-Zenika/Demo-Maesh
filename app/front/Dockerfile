
FROM python:3.7

RUN pip install flask requests

ADD app/ /app

EXPOSE 5000

CMD [ "python", "/app/app.py" ]
