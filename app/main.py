from fastapi import FastAPI , UploadFile
import  tensorflow as tf
import numpy as np
from PIL import Image
import io
app = FastAPI()

model = tf.keras.models.load_model('model.h5')

@app.get("/")
def home():
    return {"It is working."}

@app.post("/predict")
async def check(file:UploadFile):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image_resized = image.resize((256, 256))
    file = np.array([image_resized])/255
    pred=model.predict(file, verbose=0)
    if pred[0,0] >= 0.5:
        return {
            "msg": "COVID-19 found. Consult a docter",
            "code":1
            }
    else :
        return {
            "msg": "COVID-19 not found. You are fine!!",
            "code":0
                }
