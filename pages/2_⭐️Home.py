import streamlit as st

# Setting the font to monospace
st.markdown(
    """
    <style>
    * {
        font-family: monospace !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add custom CSS for the gradient background
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

# Ensure only logged-in users can access this page
if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop()  # Stops the rest of the page from loading!!!!

# Replace the title with the mainpage.png image
try:
    st.image("mainpage.png", width=400)  # Display the image without caption or border
except FileNotFoundError:
    st.error("Image not found. Please ensure 'mainpage.png' is in the correct directory.")

# Subheader and description
st.subheader("Welcome! You are now logged in. Frolick Around!")
st.write("Tired of searching for school-related activities or filling out endless forms? Frolick Finder is here to optimize your event-finding experience! Whether you're a Queen's event attendee or organizer, our platform saves you time and money by streamlining the process. With just a click, explore a wide range of campus events and experience two tailored interfaces for attendees and organizers. Say goodbye to hassle and hello to fun, affordable local activities – all in one place!")