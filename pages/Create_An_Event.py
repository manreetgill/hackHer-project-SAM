import streamlit as st
import sqlite3
from datetime import datetime

st.title("📅 Event Posting Page")

# Initialize database
def init_db():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    club TEXT,
                    date TEXT,
                    time TEXT,
                    location TEXT,
                    description TEXT,
                    image BLOB)''')
    conn.commit()
    conn.close()

# Save event to database
def save_event(title, club, date, time, location, description, image):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    image_bytes = image.read() if image else None
    
    c.execute("INSERT INTO events (title, club, date, time, location, description, image) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (title, club, date, time, location, description, image_bytes))
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Input fields
event_title = st.text_input("Event Title")
club_name = st.text_input("Organizing Club/Association")
event_date = st.date_input("Event Date", min_value=datetime.today())
event_time = st.time_input("Event Time")
location = st.text_input("Event Location")
description = st.text_area("Event Description")
image = st.file_uploader("Upload Event Poster", type=["png", "jpg", "jpeg"])

# Submit button
if st.button("Post Event"):
    save_event(event_title, club_name, event_date.strftime('%B %d, %Y'), event_time.strftime('%I:%M %p'), location, description, image)
    st.success("✅ Event Posted Successfully!")
