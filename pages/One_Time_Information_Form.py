import streamlit as st

st.title("Inputing Your Information")
st.text_input("First Name: ")
st.text_input("Last Name: ")
st.number_input("Year of Study: ", min_value=1, max_value=5, value=1, step=1)
st.text_input("Program: ")
st.text_input("Queen's Email: ")
st.text_input("Personal Email: ") 
