import streamlit as st
import pandas as pd
import numpy as np
import csv
import time
from streamlit_option_menu import option_menu

st.set_page_config("My Streamlit App")
st.title("Dashboard")
st.header("Introduction")
st.subheader("Key Metrics")
st.write ("IDK what it does.")
st.markdown("**Hello** *Bye*")

with st.sidebar:
  color = st.multiselect("Favourite colors", ["Red", "Green", "Blue"], default = ["Red"])
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

tab1, tab2, tab3 = st.tabs(["Plot", "Data", "Chart"])

with tab1:
  st.write("Here goes a chart")
  st.metric("Sales", f"1000 +5%")
  
  sales = {"Product": ["A", "B"], "Sales": [100,200]}
  df = pd.DataFrame(sales)
  st.write (f"Sum: {df["Sales"].sum()}")
  filtered = df[df["Product"].isin(["A", "C"])]
  st.dataframe(filtered)

  st.table(sales)
  st.data_editor(filtered)

  st.write("Here goes a table.")
  with st.form(key = "user_form"):
    email = st.text_input("Email")
    score = st.number_input("Score", min_value = 0, max_value =100)
    submit = st.form_submit_button("Submit")
  if submit:
    st.success(f"Email: {email}, Score: {score}")
  
  file = st.file_uploader("Upload a csv file", type = "csv")
  if file:
    st.dataframe(file)
  else:
    st.write("Please upload a CSV file")
  
  placeholder = st.empty()
  while True:
    placeholder.write(f"A new number: {np.random.randint(1,11)}")
    time.sleep(2)

  
  

with tab2:

  st.write("Here goes a table.")
  with st.form(key = "user_form"):
    email = st.text_input("Email")
    score = st.number_input("Score", min_value = 0, max_value =100)
    submit = st.form_submit_button("Submit")
  if submit:
    st.success(f"Email: {email}, Score: {score}")
  
  file = st.file_uploader("Upload a csv file", type = "csv")
  if file:
    st.dataframe(file)
  else:
    st.write("Please upload a CSV file")

with tab3:
  
  data = pd.DataFrame({
    "Period": [1,2,3,4],
    "Sales": [10, 20, 15, 30],
    "Profit": [5, 10, 8, 20]}).set_index("Period")

  st.line_chart(data)
  st.area_chart(data)
  st.bar_chart(data)
  st.scatter_chart(data[["Sales", "Profit"]].set_index("Sales"))

  
  
option = option_menu("Main Menu", options =["Home", "Settings", "About"],
                    icons = ["house", "gear", "info-cicle"],
                    default_index = 0)
if option == "Home":
  st.write("You are on the Home page")

elif option == "Settings":
  st.write("You are on the Settings page")

elif option == "About":
  st.write("You are on the About page")
  







  








