import streamlit as st
import os
print(os.getcwd())

#intializing the session state for login status 
if "login" not in st.session_state:
    st.session_state.login = False


# Title Page
st.set_page_config(page_title="Welcome!", page_icon="🔒", layout="centered")
        
# App title
st.title("Welcome to Frolick Finder!")

st.image("frolickfinder.png", width=600) 

st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;  /* Set background color */
        font-size: 18px;            /* Increase font size */
    }
    .stButton>button {
        background-color: #ff6347;  /* Change button color */
        color: white;
    }
    .css-ffhzg2 {
        max-width: 1200px;  /* Set max width for the whole layout */
        margin: 0 auto;     /* Center the content */
    }
    .signup-box {
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 20px;
        background-color: white;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Create two columns: one for the logo and one for the login/signup form
col1, col2 = st.columns([0.6, 0.4])  # Adjust the width ratio (1:3)

with col1:
    # Display the logo/image on the left (adjust width to suit)
    st.image("frolickfinder.png", width=800)

with col2:
    # Toggle between Sign In and Sign Up with circular button
    choice = st.radio("Choose an option:", ["Sign In", "Sign Up"])

    # Session state works as a dictionary, accessing usernames (ex. if username does not exist in dictionary, it will give an error/tell users to put new input)
    if "users" not in st.session_state:
        st.session_state.users = {}

    if choice == "Sign In":
        st.subheader("Sign In")
            
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
            

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
                st.success("Account created successfully! Please sign in.")



# Define pages

'''
def page_1():
    st.title("Page 1")
    st.write("This is page 1.")

def page_2():
    st.title("Page 2")
    st.write("This is page 2.")

def page_3():
    st.title("Page 3")
    st.write("This is page 3.")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("Page 1"):
    st.session_state.page = "Page 1"
if st.sidebar.button("Page 2"):
    st.session_state.page = "Page 2"
if st.sidebar.button("Page 3"):
    st.session_state.page = "Page 3"

# Display the selected page
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Page 1":
    page_1()
elif st.session_state.page == "Page 2":
    page_2()
elif st.session_state.page == "Page 3":
    page_3()
'''