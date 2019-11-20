FROM python:3-slim

ADD server.py /

RUN pip install pyzmq

CMD [ "python", "./server.py" ]

