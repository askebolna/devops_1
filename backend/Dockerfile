FROM python:3.15.0a7-alphine3.23

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY app.py .

EXPOSE 8080

CMD ["python3", "app.py"]
