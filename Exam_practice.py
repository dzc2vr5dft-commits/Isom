import streamlit as st
import pandas as pd
import numpy as np
import csv
import time

st.set_page_config("My Streamlit App")
st.title("Dashboard")
st.header("Introduction")
st.subheader("Key Metrics")
st.write ("IDK what it does.")
st.markdown("**Hello** *Bye*")

with st.sidebar:
  color = st.multiselect("Favourite colors", ["Red", "Green", "Blue"], default = "Red")
  features = st.checkbox("Enable extra features", value = True)
  number = st.slider("A slider", min_value = 0, max_value = 100, value = 50)

st.write(f"Your favourite colour: {color}")
st.write(f"Enable extra features: {features}")
st.write(f"Slider number: {number}")

name = st.text_input("Name")
age = st.number_input("Age", min_value = 1, max_value = 120)
button =st.button("Submit")
if button:
  st.success(f"Hello {name}, you are {age} years old.")

col1, col2, col3 = st.columns(3)
with col1:
  bt1 = st.button("A")

with col2:
  bt2 = st.button("B")
with col3:
  bt3 = st.button("C")

tab1, tab2 = st.tabs(["Plot", "Data"])

with tab1:
  st.write("Here goes a chart")
  st.metric("Sales", f"1000 +5%")
  placeholder = st.empty()
  while True:
    placeholder.write(f"A new number: {np.random.randint(1,11)})
    time.sleep(2)

with tab2:
  st.write("Here goes a table.")










  








