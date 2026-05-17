import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Business Performance Dashboard")
st.write("Demostrate business dashboard")

col1, col2, col3 = st.columns(3)
revenue = {"Q1": 1.2, "Q2": 1.5, "Q3": 1.3, "Q4": 2}
comments = ["Hi", "Bye", "IDK"]
trends = ["Choco", "eco-friendly", "tesla"]
with col1:
  st.header("Q1")
  st.write(f"${revenue["Q1"]}M")

with col2:
  st.header("Q2")
  st.write(f"${revenue["Q2"]}M")

with col3:
  st.header("Q3")
  st.write(f"${revenue["Q3"]}M")

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])

with tab1:
  for a,b in revenue.items():
    st.write(f"{a}: ${b}M")

with tab2:
  for a,b in enumerate(comments,1):
    st.write(f"{a}. {b}")

with tab3:
  for a,b in enumerate(trends,1):
    st.write(f"{a}. {b}")

with st.expander("More Information"):
  st.write("The data is collected from nowhere.")

placeholder = st.empty()

for i in range(5):
  
  placeholder.write(f"Loading data...{i*20}% complete")
  
  time.sleep(1)

placeholder.write("There is no business insights.")

box = st.selectbox("Select a box", ["Q1", "Q2", "Q3", "Q4"])

growth = st.slider("Growth", min_value = 0, max_value=100)
st.metric(f"${revenue[box]*(1+growth/100):,.2f}M")

st.bar_chart(revenue, x="Quarter", y="Revenue")
button = st.button("Click")
if button:
  st.success("Keep pushing for growth!")


  






