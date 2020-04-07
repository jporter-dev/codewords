FROM python:3.7-stretch

WORKDIR /app
ENV FLASK_APP __init__.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV HOST 0.0.0.0
EXPOSE 5000
CMD ["python", "__init__.py"]
