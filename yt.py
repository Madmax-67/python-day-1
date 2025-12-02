import streamlit as st

st.title("YouTube Demo in Streamlit")

st.write("Here is an embedded YouTube video:")

# Replace with any YouTube URL you want
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

st.video(youtube_url)

st.write("""
You can embed any YouTube link using `st.video(url)`.
""")
