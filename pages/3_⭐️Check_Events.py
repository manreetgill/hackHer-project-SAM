import streamlit as st
import sqlite3
from PIL import Image
import io
#We used Steamlit Documentation to figure out most of this!
#CSS bits taken from online (e.g, HEX codes, syntax) for all pages that include it

# Setting the font to monospace
st.markdown(
    """
    <style>
    /* Change font to monospace for the entire app */
    * {
        font-family: monospace !important;
    }

    /* Change text color to white for the main page only */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp p, .stApp div {
        color: white !important;
    }

    /* Ensure sidebar text remains unaffected */
    .css-1d391kg * {
        color: inherit !important; /* Use the default sidebar text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#Adding custom CSS for the blue/yellow gradient background
st.markdown(
    """
    <style>
    .stApp {
        background: rgb(251,187,63);
        background: radial-gradient(circle, rgba(251,187,63,1) 0%, rgba(164,221,237,1) 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Ensure only logged-in users can access this page
if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop()  # Stops the rest of the page from loading!!!!

#events.png is the title
try:
    st.image("events.png", width=400)  # Display the image without caption or border
except FileNotFoundError:
    st.error("Image not found. Please ensure 'events.png' is in the correct directory.")

#SQL-like Database functions we learned from online videos
#Function to load events from database 
def load_events():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT title, club, date, time, location, description, image FROM events")
    events = c.fetchall()
    conn.close()
    return events

#Load events
events = load_events()

if not events:
    st.info("No events posted yet. Go to the event posting page to add one!")
else:
    cols = st.columns(3)  # Creates a 3-column grid

    for index, event in enumerate(events):
        col = cols[index % 3]  # Distribute events evenly across columns
        with col:
            # Use st.expander to create a collapsible section for each event
            with st.expander(f"**{event[0]}**", expanded=False):
                # Display image if available
                if event[6]:
                    image = Image.open(io.BytesIO(event[6]))
                    st.image(image, use_container_width=True)

                st.write(f"**Organized by:** {event[1]}")
                st.write(f"📅 **Date:** {event[2]}")
                st.write(f"⏰ **Time:** {event[3]}")
                st.write(f"📍 **Location:** {event[4]}")
                st.write(f"**Description:** {event[5]}")