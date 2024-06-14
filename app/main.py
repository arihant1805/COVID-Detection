from fastapi import FastAPI , UploadFile
import  tensorflow as tf
import cv2 as cv
import numpy as np

app = FastAPI()

model = tf.keras.models.load_model('model.h5')

@app.get("/")
def home():
    return {"It is working."}

@app.post("/predict")
async def check(file:UploadFile):
    contents = await file.read()
    np_img = np.fromstring(contents, np.uint8)
    image = cv.imdecode(np_img, cv.IMREAD_COLOR)
    file_resized = cv.resize(image, (256, 256))
    file = np.array([file_resized])
    pred=model.predict(file)
    if pred[0] >= 0.5:
        return {"msg": "COVID-19 found. Consult a docter"}
    else :
        return {"msg": "COVID-19 not found. You are fine!!"}
