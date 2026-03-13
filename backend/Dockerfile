FROM python:3.15.0a7-alpine3.23

RUN adduser -D appuser

WORKDIR /app

COPY app.py .

RUN chmod 444 app.py && chown root:root app.py

USER appuser

EXPOSE 8080

CMD ["python3", "app.py"]
