import streamlit as st
import sqlite3
from PIL import Image
import io

# Setting the font to monospace
st.markdown(
    """
    <style>
    * {
        font-family: monospace !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!
    
st.title("📅 Event Gallery")

# Function to load events from database ## defo look into this cause what is tissss
def load_events():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT title, club, date, time, location, description, image FROM events")
    events = c.fetchall()
    conn.close()
    return events

# Load events
events = load_events()

if not events:
    st.info("No events posted yet. Go to the event posting page to add one!")
else:
    cols = st.columns(3)  # Creates a 3-column grid
    
    for index, event in enumerate(events):
        col = cols[index % 3]  # Distribute events evenly across columns
        with col:
            st.subheader(event[0])  # Title
            
            # Display image if available
            if event[6]:
                image = Image.open(io.BytesIO(event[6]))
                st.image(image, use_column_width=True)
            
            st.write(f"**Organized by:** {event[1]}")
            st.write(f"📅 {event[2]} ⏰ {event[3]}")
            st.write(f"📍 {event[4]}")
            st.write(event[5])
