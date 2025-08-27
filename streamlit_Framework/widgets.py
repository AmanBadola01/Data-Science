import streamlit as st

st.title("Streamlit Text input")

name= st.text_input("Enter you name:")

age= st.slider("Select your age:",0,100,25)

if name:
    st.write(f"Hello {name}")
    st.write(f"Your age is {age}")

