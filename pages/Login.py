import streamlit as st

if st.button("Login"):
    if username in st.session_state.users and st.session_state.users[username] == password:
        st.success(f"Welcome back, {username}!")
        #setting the state to true for web page navigation
        st.session_state.login = True
        #Redirect to switch page to main
        st.switch_page("pages/main_page.py")
    else:
        st.error("Invalid username or password.")
        