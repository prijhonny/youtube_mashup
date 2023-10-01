import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import urllib.request
import re
import os

def mash(x, n, y):
    delete_after_use = True
    x = x.replace(' ','') + "songs"
    n, y = int(n), int(y)  # assuming n and y are always valid integers when this function is called
    output_name = 'output.mp3'
    
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + str(x))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for i in range(n):
        yt = YouTube("https://www.youtube.com/watch?v=" + video_ids[i]) 
        st.write(f"Downloading File {i+1} .......")
        mp4files = yt.streams.filter(only_audio=True).first().download(filename='tempaudio-'+str(i)+'.mp3')

    st.write("Files downloaded.")
    st.write("Getting the mashup ready.....")

    if os.path.isfile("tempaudio-0.mp3"):
        fin_sound = AudioSegment.from_file("tempaudio-0.mp3")[0:y*1000]
    for i in range(1,n):
        aud_file = str(os.getcwd()) + "/tempaudio-"+str(i)+".mp3"
        fin_sound = fin_sound.append(AudioSegment.from_file(aud_file)[0:y*1000],crossfade=1000)
  
    fin_sound.export(output_name, format="mp3")
    st.write(f"File downloaded successfully. Stored as {output_name}")
        
    if delete_after_use:
        for i in range(n):
            os.remove("tempaudio-"+str(i)+".mp3")

# Streamlit interface
st.title("YouTube Audio Mashup")
query = st.text_input("Enter the search query:")
n = st.slider("Number of songs:", 1, 10, 1)
y = st.slider("Duration in seconds:", 1, 600, 10)
if st.button("Generate Mashup"):
    try:
        mash(query, n, y)
        audio_file = open('output.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    except Exception as e:
        st.error(f"An error occurred: {e}")
