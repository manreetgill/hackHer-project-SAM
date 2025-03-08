import streamlit as st
from PIL import Image
import io



st.title("📅 Event Gallery")

# Check if there are events stored
if "events" not in st.session_state or not st.session_state["events"]:
    st.info("No events posted yet. Go to the event posting page to add one!")
else:
    events = st.session_state["events"]
    
    # Display events in a grid
    cols = st.columns(3)  # Creates a 3-column grid
    
    for index, event in enumerate(events):
        col = cols[index % 3]  # Distribute events evenly across columns
        with col:
            st.subheader(event["title"])
            
            # Display image if uploaded
            if event["image"]:
                image = Image.open(event["image"])
                st.image(image, use_column_width=True)
            
            st.write(f"**Organized by:** {event['club']}")
            st.write(f"📅 {event['date']} ⏰ {event['time']}")
            st.write(f"📍 {event['location']}")
            st.write(event['description'])
