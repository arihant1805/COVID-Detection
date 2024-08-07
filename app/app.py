import requests
import streamlit as st
from PIL import Image
import io

st.title("Upload the X-ray of the chest,for COVID-19 detection:")
st.write("to try out download any image from [Sample Image](https://github.com/arihant1805/COVID-Detection/blob/master/SampleImage.jpeg) or from the [Kaggle DataSet](https://www.kaggle.com/datasets/khoongweihao/covid19-xray-dataset-train-test-sets)")

file = st.file_uploader("Choose a file")
if file is not None:
    file_bytes = file.read()
    image = Image.open(io.BytesIO(file_bytes))
    st.image(image, caption="Uploaded image", width=300)
    files = {"file": (file.name, file_bytes, file.type)}
    x = requests.post('https://covid-19-detection-1d3l.onrender.com/predict', files=files)
    if x.status_code == 200:
        data = x.json()
        data = str(data['msg'])
        st.title(data)
    else:
        st.error("An error occurred while processing the uploaded file.")