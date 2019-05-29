FROM python:3.6-alpine

RUN adduser -D mediate

WORKDIR /home/mediate

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY mediate.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP mediate.py

RUN chown -R mediate:mediate ./
USER mediate

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
