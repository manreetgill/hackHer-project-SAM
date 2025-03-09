import streamlit as st

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

#st.set_page_config(page_title="Main Page", page_icon="🏠", layout="centered")

#Ensure only logged-in users can access this pafe
if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!

st.title("Main Page")
st.subheader("Welcome! You are now logged in. Frolick Around!")
st.write("Tired of searching for school-related activities or filling out endless forms? Frolick Finder is here to optimize your event-finding experience! Whether you're a Queen's event attendee or organizer, our platform saves you time and money by streamlining the process. With just a click, explore a wide range of campus events and experience two tailored interfaces for attendees and organizers. Say goodbye to hassle and hello to fun, affordable local activities – all in one place!")
