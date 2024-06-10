import tensorflow as tf
from fastapi import FastAPI, File
from tensorflow.keras.models import load_model
import cv2 as cv
import numpy as np

model = load_model('model.h5')

app = FastAPI()

@app.post("/")
def check(file : File):
    img = cv.resize(file, (256, 256))
    img = np.array([img])
    pred = model.predict(img)[0]

    if pred >= 0.5:
        return {"You have corona."}
    
    else:
        return {"You are healthy"}
