FROM python:3.11.9-alpine
COPY . /app
WORKDIR /app/app
RUN pip install -r requirements.txt 
CMD ["uvicorn", "main:app"]