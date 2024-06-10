FROM python:3.6.5-slim
RUN apt-get update && apt-get install -y
COPY . /app
WORKDIR /app/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app"]