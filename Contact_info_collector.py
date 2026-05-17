import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("Contact Info Collector")
contact = []
with st.form(key="my_form"):
  
    first_name = st.text_input("First name:").title()
    last_name = st.text_input("Last name:").title()
    no = st.number_input("Favorite number:")
    button = st.form_submit_button("Register")
    if button:
      try:
        if first_name.strip() == "" or last_name.strip() == "":
          raise ValueError
        no = int(no)
    
      except ValueError:
        print("Invalid input.")
      except Exception as i:
        print(i)
      else:
        contact.append({"First Name": first_name, "Last Name": last_name, "Favorite Number": no})
        data =pd.DataFrame(contact)
        st.dataframe(data)
        st.success("Data added successfully!")







