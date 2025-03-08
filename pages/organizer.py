import streamlit as st
from datetime import datetime

st.title("Event Posting Page")

# Input fields
event_title = st.text_input("Event Title")
club_name = st.text_input("Organizing Club/Association")
event_date = st.date_input("Event Date", min_value=datetime.today())
event_time = st.time_input("Event Time")
location = st.text_input("Event Location")
description = st.text_area("Event Description")

# Image upload
image = st.file_uploader("Upload Event Poster", type=["png", "jpg", "jpeg"])

# Submit button
if st.button("Post Event"):
    st.subheader("📢 Event Details")
    st.write(f"**Title:** {event_title}")
    st.write(f"**Organized by:** {club_name}")
    st.write(f"**Date:** {event_date.strftime('%B %d, %Y')}")
    st.write(f"**Time:** {event_time.strftime('%I:%M %p')}")
    st.write(f"**Location:** {location}")
    st.write("**Description:**")
    st.write(description)
    
    if image:
        st.image(image, caption="Event Poster", use_column_width=True)
