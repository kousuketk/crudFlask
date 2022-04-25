FROM python:3.9

COPY ./src ./src
WORKDIR /src
RUN pip install flask
RUN pip install PyMySQL
CMD ["python", "hello.py"]