FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/work


COPY ./lib.txt /usr/src/lib.txt
RUN pip install -r /usr/src/lib.txt

COPY . /usr/src/work

EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]