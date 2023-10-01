import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import urllib.request
import re
import os

def mash(x, n, y):
    # ... [The rest of your mash function remains unchanged] ...

# Streamlit interface for gathering user inputs
st.title("YouTube Audio Mashup")

# Text box for the search query
query = st.text_input("Enter the search query:")

# Slider for selecting the number of songs (from 1 to 10)
n = st.slider("Number of songs:", 1, 10, 1)

# Slider for selecting the desired duration in seconds (from 1 to 600 seconds)
y = st.slider("Duration in seconds:", 1, 600, 10)

# Button to initiate the mashup process
if st.button("Generate Mashup"):
    try:
        mash(query, n, y)
        st.success("Mashup created successfully!")
        audio_file = open('output.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    except Exception as e:
        st.error(f"An error occurred: {e}")

