
FROM python:3.7

RUN pip install Flask flask_restful  

ADD app/ /app

EXPOSE 5000

CMD [ "python", "/app/app.py" ]
