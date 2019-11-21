FROM python:3-slim

COPY . /

ENV FLASK_APP="server.py"

# install dependencies
RUN pip install -r requirements.txt --no-cache-dir

CMD [ "flask", "run" ]
