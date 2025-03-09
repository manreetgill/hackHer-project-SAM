import streamlit as st
#We used Steamlit Documentation to figure out most of this!
#CSS bits taken from online (e.g, HEX codes, syntax) for all pages that include it

#Setting the font to monospace
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

#Adding custom CSS for the blue/yellow gradient background (used outside sources for the CSS backgrounds)
st.markdown(
    """
    <style>
    .stApp {
        background: rgb(251,187,63);
        background: radial-gradient(circle, rgba(251,187,63,1) 0%, rgba(164,221,237,1) 100%);
    }

    /* Style for square buttons */
    .stButton>button {
        width: 100%;
        height: 100px; /* Fixed height for square buttons */
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        background-color: #a4dded; /* Light blue background */
        color: white; /* White text */
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #74b0e4; /* Darker blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Initializing session state (boolean) for login status, users, and current user
if "login" not in st.session_state:
    st.session_state.login = False

if "users" not in st.session_state:
    st.session_state.users = {}  #Dictionary to store users and their role, this will add them if they don't already exist

if "current_user" not in st.session_state:
    st.session_state.current_user = None  #Initialize current_user

#App title and header
try:
    st.image("welcome.png", width=400)  #Display the image without caption or border
except FileNotFoundError:
    st.error("Image not found. Please ensure 'welcome.png' is in the correct directory.")

#Check if the user is logged in
if not st.session_state.login:
    st.subheader("Please sign in to continue.")

    #Create three square buttons using columns (same way as before)
    col1, col2, col3 = st.columns(3)  #Three equal-width columns

    with col1:
        if st.button("Sign In"):
            st.session_state.choice = "Sign In"

    with col2:
        if st.button("Sign Up as General User"):
            st.session_state.choice = "Sign Up as General User"

    with col3:
        if st.button("Sign Up as Event Organizer"):
            st.session_state.choice = "Sign Up as Event Organizer"

    #Handle the selected choice
    if "choice" in st.session_state:
        if st.session_state.choice == "Sign In":
            st.subheader("Sign In")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if email in st.session_state.users and st.session_state.users[email]["password"] == password:
                    st.success(f"Welcome back, {email}!")
                    st.session_state.login = True
                    st.session_state.current_user = {
                        "email": email,
                        "role": st.session_state.users[email]["role"]
                    }
                    st.switch_page("pages/2_⭐️Home.py")  #Redirect to Home page after successful login
                else:
                    st.error("Invalid email or password. ❌")

        elif st.session_state.choice == "Sign Up as General User":
            st.subheader("Sign Up as General User")
            new_email = st.text_input("Please enter your email")
            new_password = st.text_input("Choose a Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            if st.button("Register"):
                if new_email in st.session_state.users:
                    st.error("Email already taken! Try another one ❌")
                elif new_password != confirm_password:
                    st.error("Passwords do not match! ❌")
                elif not new_email or not new_password:
                    st.error("Please fill in all fields.")
                else:
                    st.session_state.users[new_email] = {"password": new_password, "role": "General User"}
                    st.success("Account created successfully! Please sign in. ✅")

        elif st.session_state.choice == "Sign Up as Event Organizer":
            st.subheader("Sign Up as Event Organizer")
            new_email = st.text_input("Please enter your email")
            new_password = st.text_input("Choose a Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            if st.button("Register"):
                if new_email in st.session_state.users:
                    st.error("Username already taken! Try another one. ❌")
                elif new_password != confirm_password:
                    st.error("Passwords do not match! ❌")
                elif not new_email or not new_password:
                    st.error("Please fill in all fields.")
                elif not new_email.endswith('@queensu.ca'):
                    st.error("Invalid email address! Event Organizers must have a valid '@queensu.ca' email address. ❌")
                else:
                    st.session_state.users[new_email] = {"password": new_password, "role": "Event Organizer"}
                    st.success("Account created successfully! Please sign in.✅")

else:
    #User is logged in, show the main app content
    if st.session_state.current_user:
        st.write(f"Welcome, {st.session_state.current_user['email']}!")
        st.write(f"Your role: {st.session_state.current_user['role']}")

    #logout button
    if st.button("👋 Logout"):
        st.session_state.login = False
        st.session_state.current_user = None
        st.rerun()  #Refresh the page to show the login form again