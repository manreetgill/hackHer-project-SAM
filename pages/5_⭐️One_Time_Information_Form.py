import streamlit as st
#We used Steamlit Documentation to figure out most of this!
#CSS bits taken from online (e.g, HEX codes, syntax) for all pages that include it

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

try:
    st.image("infoposting.png", width=400)  #infoposting.png is title
except FileNotFoundError:
    st.error("Image not found. Please ensure 'infoposting.png' is in the correct directory.")
if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!

st.text_input("First Name: ")
st.text_input("Last Name: ")
st.number_input("Year of Study: ", min_value=1, max_value=5, value=1, step=1)
st.text_input("Program: ")
st.text_input("Queen's Email: ")
st.text_input("Personal Email: ") 
