FROM python:3.11.9-alpine
RUN sudo apt update \
    sudo apt install build-essential gcc gfortran
COPY . /app
WORKDIR /app/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
CMD ["uvicorn", "main:app"]