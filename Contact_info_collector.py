import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

st.header("Contact Info Collector")

with open ("contacts.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["First Name", "Last Name", "Favorite Number"])
    writer.writeheader()
    
with st.form(key="my_form"):
    
    first_name = st.text_input("First name:").title()
    last_name = st.text_input("Last name:").title()
    no = st.number_input("Favorite number:")
    button = st.form_submit_button("Register")
    if button:
        try:
            contact = []
            if first_name.strip() == "" or last_name.strip() == "":
                raise ValueError
            no = int(no)
    
        except ValueError:
            print("Invalid input.")
        except Exception as i:
            print(i)
        else:
            contact.append({"First Name": first_name, "Last Name": last_name, "Favorite Number": no})
        
            with open ("contacts.csv", "a") as file:
                
                for i in contact:
                    writer.writerow(i)
            data = pd.read_csv("contacts.csv")
            st.success("Data added successfully!")
        
            st.dataframe(data)
          















