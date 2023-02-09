import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Deteksi Garis Tepi")
st.write("Program Deteksi Tepi dengan Canny Edge Detection OpenCV Python dan GUI streamlit webrtc")

threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)


def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

left_column, right_column = st.columns(2)

with left_column:
    webrtc_streamer(key="asli")
    
with right_column:
    webrtc_streamer(key="garis tepi", video_frame_callback=callback)