import streamlit as st
import os
#We used Steamlit Documentation to figure out most of this!
#CSS bits taken from online (e.g, HEX codes, syntax) for all pages that include it

#Set all the font to monospace
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

#Print current working directory (for debugging)
print(os.getcwd())

#Initialize session state for login status
if "login" not in st.session_state:
    st.session_state.login = False

#Add custom CSS for the gradient background
st.markdown(
    """
    <style>
    .stApp {
        background: rgb(246,196,101);
        background: radial-gradient(circle, rgba(246,196,101,1) 0%, rgba(230,148,233,1) 100%);
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #a4dded;
        color: white;
        border-radius: 10px;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: background-color 0.3s ease;
        width: 100%; /* Make buttons take full width of their container */
        height: 100px; /* Set a fixed height for square buttons */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton>button:hover {
        background-color: #74b0e4;
    }
    .stTitle {
        color: #ffffff;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Center content using Streamlit columns (interpreted as percentages or fractions, e.g., thirds)
col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider to center content

with col2:  #Put everything inside the middle column
    #App title

    #Try/except to handle image loading
    try:
        st.image("fflogo.png", use_container_width=True, output_format="PNG")  # Removed caption
    except:
        st.error("Image not found. Please check if 'fflogo.png' exists in the right directory.")

    #Create three square buttons using columns
    col4, col5, col6 = st.columns(3)  #Three equal-width columns

    #Redirect to Login.py
    with col4:
        if st.button("Sign Up as General User"):
            st.session_state.choice = "Sign Up as General User"
            st.switch_page("pages/1_⭐️Login.py") 

    with col5:
        if st.button("Sign Up as Event Organizer"):
            st.session_state.choice = "Sign Up as Event Organizer"
            st.switch_page("pages/1_⭐️Login.py")  

    with col6:
        if st.button("Sign In"):
            st.session_state.choice = "Sign In"
            st.switch_page("pages/1_⭐️Login.py")