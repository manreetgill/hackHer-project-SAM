import streamlit as st
#We used Steamlit Documentation to figure out most of this!
#CSS bits taken from online (e.g, HEX codes, syntax) for all pages that include it

#Setting the font to monospace and white for the main page only
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

#Add custom CSS for the gradient background
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

#mainpage.png is the title
try:
    st.image("mainpage.png", width=400)  # Display the image without caption or border
except:
    st.error("Image not found. Please ensure 'mainpage.png' exists and is in the right directory.")

#Subheader and description
st.subheader("Welcome! You are now logged in. Frolick Around!")
st.write("Tired of searching for school-related activities or filling out endless forms? Frolick Finder is here to optimize your event-finding experience! Whether you're a Queen's event attendee or organizer, our platform saves you time and money by streamlining the process. With just a click, explore a wide range of campus events and experience two tailored interfaces for attendees and organizers. Say goodbye to hassle and hello to fun, affordable local activities – all in one place!")