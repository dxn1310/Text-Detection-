#importing the modules
import cv2
import matplotlib.pyplot as plt
import easyocr
import streamlit as st
import numpy as np
from PIL import Image
import time


# st.write(""" # Text Detection On Image """)
st.markdown("<h1 style='text-align: center; color: white;'>Text Detection On Image</h1>", unsafe_allow_html=True)
st.write(""" ##### Upload an image and please wait for a few seconds """)

uploaded_file = st.file_uploader("Upload an image",type=("png"))

if uploaded_file != None:
    image = Image.open(uploaded_file)
    img = np.array(image)
    
    st.spinner('Wait for it...')
        # time.sleep(5)
    
    # #creating instace text detector
    reader = easyocr.Reader(['en'], gpu=True)

    # #detect the text on image
    text_ = reader.readtext(img)

    for i in text_:
        box, text, score = i

        cv2.rectangle(img,box[0],box[2],(0,255,0),2)
        cv2.putText(img,text,box[0],cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    c1, c2 = st.columns(2)

    with c1:
        st.image(uploaded_file,caption="Uploaded Image",width=350)
    with c2:
        st.image(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),caption="Text Detected on Uploaded Image",width=350)
