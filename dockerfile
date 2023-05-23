FROM python:3.11

ENV PYTHONBUFFERED=1
WORKDIR /code
COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . .
EXPOSE 8000
CMD [ "python","manage.py","runserver" ]
