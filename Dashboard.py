import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title = "My First App")


st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("Please provide your details below:")

name = st.text_input("What is your name?").title()
age = st.number_input("Enter your age:", min_value = 0, max_value = 120, value = 25)
color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])

if st.button("Submit"):
    st.success(f"{name}, thank you! Age: {age}, Favorite Color: {color}")
