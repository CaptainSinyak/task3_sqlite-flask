FROM python:3.9.1-alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN python3 config.py

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:7000", "main:app"]