import streamlit as st
from datetime import datetime
import os

# Set up the page config for Streamlit
st.set_page_config(page_title="Happy Valentine's Day, babe!", page_icon="❤️", layout="centered")

# Add CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f9e3e3;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .stButton > button {
        background-color: #ff6b6b;
        color: white;
        font-size: 18px;
        padding: 15px 30px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff4040;
    }
    .stTitle {
        font-size: 3rem;
        text-align: center;
        color: #ff6b6b;
        font-weight: bold;
        margin-top: 40px;
    }
    .stSubheader {
        font-size: 1.8rem;
        text-align: center;
        color: #ff4040;
    }
    .stMarkdown {
        font-size: 1.3rem;
        text-align: center;
    }
    .stVideo {
        border-radius: 10px;
        max-width: 100%;
        margin: 30px auto;
    }
    footer {
        text-align: center;
        margin-top: 50px;
        font-size: 1rem;
        color: #666;
    }
    .countdown {
        font-size: 1.5rem;
        text-align: center;
        font-weight: bold;
        color: #ff6b6b;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display a header and introductory message
st.title("Happy Valentine's Day, [Babe]!")
st.subheader("Here's a little something special just for you.")

# Add an image (optional)
# st.image("images/img1.jpg", caption="Our memories together", use_column_width=True)

# Add video
st.subheader("Our Special Video 🎥")
video_file = open("assets/your-video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Interactive message
st.subheader("A Message Just For You 💌")
if st.button("Click me for a surprise"):
    st.write("You make my heart skip a beat every day! 💖")

# Countdown timer (for next Valentine’s Day or a special date)
countdown_date = datetime(2026, 2, 14)  # Set the target date

now = datetime.now()
remaining_time = countdown_date - now

days_left = remaining_time.days
hours_left = remaining_time.seconds // 3600
minutes_left = (remaining_time.seconds // 60) % 60
seconds_left = remaining_time.seconds % 60

st.subheader("Countdown to Our Next Adventure:")
st.markdown(f"<div class='countdown'>{days_left} Days, {hours_left} Hours, {minutes_left} Minutes, {seconds_left} Seconds</div>", unsafe_allow_html=True)

# Footer message
st.markdown("---")
st.write("Created with ❤️ by your Love")

