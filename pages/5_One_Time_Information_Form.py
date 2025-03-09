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

st.title("Inputing Your Information")

if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!

st.text_input("First Name: ")
st.text_input("Last Name: ")
st.number_input("Year of Study: ", min_value=1, max_value=5, value=1, step=1)
st.text_input("Program: ")
st.text_input("Queen's Email: ")
st.text_input("Personal Email: ") 
