FROM python:3.8.5-alpine
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
ADD src/ /app
CMD ["python", "app.py" ]