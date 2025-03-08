import streamlit as st

# Title Page
st.set_page_config(page_title="Welcome!", page_icon="🔒", layout="centered")

# App title
st.title("Welcome to Frolick Finder!")

# Toggle between Sign In and Sign Up with circular button
choice = st.radio("Choose an option:", ["Sign In", "Sign Up"])

# Session state works as a dictionary, accessing usernames (ex. if username does not exist in dictionary, it will give an error/tell users to put new input)
if "users" not in st.session_state:
    st.session_state.users = {}

if choice == "Sign In":
    st.subheader("Sign In")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password.")

elif choice == "Sign Up":
    st.subheader("Sign Up")
    
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Register"):
        if new_username in st.session_state.users:
            st.error("Username already taken! Try another one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match!")
        elif not new_username or not new_password:
            st.error("Please fill in all fields.")
        else:
            st.session_state.users[new_username] = new_password
            st.success("Account created successfully! Now sign in.")

