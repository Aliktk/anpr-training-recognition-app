import streamlit as st
from PIL import Image
import os

# Error handling for image loading
try:
    image = Image.open('plates.jpg')
except FileNotFoundError:
    st.error("Error: 'plates.jpg' not found. Please ensure the image file is in the correct directory.")
    image = None

# Page title and main image
st.title('🚗 Automatic Number Plate Recognition (ANPR) with YOLOv8')

if image:
    st.image(image, caption='Sample License Plate Detection')

# Introduction Section
st.subheader('Welcome to the ANPR System')

st.markdown("""
<span style='font-size: 18px; font-weight: 500;'>This project uses the YOLOv8 model for automatic number plate recognition (ANPR). 
It allows you to upload images or videos of vehicles, detect license plates, and save the results in a CSV file.</span>
""", unsafe_allow_html=True)

# Instructions for Use
st.markdown("""
### Features:
- 🖼️ **Image Detection**: Upload an image of a vehicle, and the system will extract the license plate number.
- 🎥 **Video Detection**: Upload a video, and the system will detect and track all vehicle license plates.
- 📊 **Data Storage**: All detected license plates are automatically saved in a CSV file for your records.
""")

# Navigation links
st.markdown("""
<ul style='font-size: 18px;'>
  <li>📘 Connect with the creator: <a href="https://www.linkedin.com/in/ali-nawaz-khattak/"target="_blank" style="text-decoration: none; color: #0073b1;">Ali Nawaz</a></li>
  <li>💻 Explore the source code on: <a href="https://github.com/Aliktk/" target="_blank" style="text-decoration: none; color: #0073b1;">GitHub</a></li>
</ul>
""", unsafe_allow_html=True)

# Footer with error handling for missing sections
if not os.path.exists('plates.jpg'):
    st.warning("Note: The sample image is missing. Please upload your own image or video for detection.")
