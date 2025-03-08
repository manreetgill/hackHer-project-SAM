import streamlit as st
if not st.session_state.get("login", False):  # Default to False if "login" is not set
    st.error("You must be logged in to access this page.")
    st.stop()

st.title("TESTING")
st.write("you should only be able to access this if you're logged in. ")