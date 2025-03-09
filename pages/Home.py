import streamlit as st

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="centered")

#Ensure only logged-in users can access this pafe
if "login" not in st.session_state or not st.session_state.login:
    st.error("You must be logged in to access this page.")
    st.stop() #Stops the rest of the page from loading!!!!

st.title("Main Page")
st.write("Welcome! You are now logged in. Frolick Around!")