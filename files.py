import streamlit as st
import pandas as pd

st.header("Manohar")

st.subheader("Uploading files - csv/xlsx")

df = st.file_uploader("Upload csv file:", type = ['csv','xlsx'])
    
df1 = pd.read_csv("data.csv")
st.table(df1)


# direcly with image-------------------------------------------------------------
st.subheader("Uploading an image in our app")

# users upload the image file------------------------------------------------------------------
# and displaying the image
st.subheader("Working with images")

img = st.file_uploader("Upload the Image file:", type = ['png','jpg'])
if img != None:
    st.image(img)# displaying the image


#----------------------------------------------------------------------------------------

# working with videos
st.subheader("Working with videos")

vid = st.file_uploader("Upload the Video file:", type = ['mkv','mp4'])

if vid is not None:
    st.video(vid, start_time= 5)

#----------------------------------------------------------------------------------------
# audio files

st.subheader("Audio Files")
aud = st.file_uploader("Upload the Audio File:", type =['mp3','wav'])
if aud is not None:
    st.audio(aud)# can also give aud.read() instead of aud
    



















