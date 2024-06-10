FROM python:3.6.5-alpine
RUN sudo apt-get update
COPY . /app
WORKDIR /app/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app"]