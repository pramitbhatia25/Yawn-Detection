import requests
import streamlit as st
from io import StringIO
import os
def save_uploadedfile(uploadedfile):
     with open("image.jpg","wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

with st.sidebar:
    st.title("Yawn Image Detection")
    st.info("This app lets you click an image and predict if the person in the image is yawning or not.")
    st.info("The image is being sent to a Flask API, which uses a trained Deep Learning Model to make a prediction.")

datafile = st.camera_input("Take a picture")

if datafile is not None:
    file_details = {"FileName":datafile.name,"FileType":datafile.type}
    save_uploadedfile(datafile)

    url = 'http://127.0.0.1:5000/'
    
    my_img = {'image': open("image.jpg", 'rb')}
    r = requests.post(url, files=my_img)
    st.write(r.json()['ans'])
    st.write(r.json()['prob'])

