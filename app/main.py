import tensorflow as tf
from fastapi import FastAPI, 
from tensorflow.keras.models import load_model

model = load_model('model.h5')

app = FastAPI()

@app.post("/")
def check(file :)

