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

# Set page configuration
#st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")

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

# Initialize session state for login status, users, and current user
if "login" not in st.session_state:
    st.session_state.login = False

if "users" not in st.session_state:
    st.session_state.users = {}  # Dictionary to store users and their roles

if "current_user" not in st.session_state:
    st.session_state.current_user = None  # Initialize current_user

# App title and header
st.title("Welcome to Frolick Finder!")

# Check if the user is logged in
if not st.session_state.login:
    st.subheader("Please sign in to continue.")

    # Choice between Sign In, Sign Up as General User, and Sign Up as Event Organizer
    choice = st.radio("Choose an option:", ["Sign In", "Sign Up as General User", "Sign Up as Event Organizer"])

    # Normal Sign In
    if choice == "Sign In":
        st.subheader("Sign In")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username in st.session_state.users and st.session_state.users[username]["password"] == password:
                st.success(f"Welcome back, {username}!")
                # Set login state to True
                st.session_state.login = True
                # Store the current user's data in session state
                st.session_state.current_user = {
                    "username": username,
                    "role": st.session_state.users[username]["role"]
                }
                # Redirect to the main page
                st.switch_page("pages/2_⭐️Home.py")
            else:
                st.error("Invalid username or password. ❌")

    # General User Sign-Up
    elif choice == "Sign Up as General User":
        st.subheader("Sign Up as General User")
        
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.button("Register"):
            if new_username in st.session_state.users:
                st.error("Username already taken! Try another one ❌")
            elif new_password != confirm_password:
                st.error("Passwords do not match! ❌")
            elif not new_username or not new_password:
                st.error("Please fill in all fields.")
            else:
                st.session_state.users[new_username] = {"password": new_password, "role": "General User"}
                st.success("Account created successfully! Please sign in. ✅")

    # Event Organizer Sign-Up
    elif choice == "Sign Up as Event Organizer":
        st.subheader("Sign Up as Event Organizer")
        
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
                st.session_state.users[new_username] = {"password": new_password, "role": "Event Organizer"}
                st.success("Account created successfully! Please sign in. ✅")

else:
    # User is logged in, show the main app content
    if st.session_state.current_user:
        st.write(f"Welcome, {st.session_state.current_user['username']}!")
        st.write(f"Your role: {st.session_state.current_user['role']}")

    # Example: Add a logout button
    if st.button("👋 Logout"):
        st.session_state.login = False
        st.session_state.current_user = None
        st.rerun()  # Refresh the page to show the login form again