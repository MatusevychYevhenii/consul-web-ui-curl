FROM python:3.6-alpine

RUN pip install flask

RUN pip install requests

COPY src /app

WORKDIR /app

RUN chmod +x consul.py

EXPOSE 80

ENTRYPOINT ["./consul.py"]
