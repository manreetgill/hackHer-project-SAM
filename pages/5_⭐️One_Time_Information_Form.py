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

# Adding custom CSS for the blue/yellow gradient background
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

st.title("Inputting Your Information")

if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!

st.text_input("First Name: ")
st.text_input("Last Name: ")
st.number_input("Year of Study: ", min_value=1, max_value=5, value=1, step=1)
st.text_input("Program: ")
st.text_input("Queen's Email: ")
st.text_input("Personal Email: ") 
