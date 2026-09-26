#Create a small dashboard with:
#1->Title + Description 
import streamlit as st
title = st.title("Simple Sales Dashboard")
Description = st.write("Analze your the Sales performance and product information")

#2->A selectbox months:
months = st.selectbox("month",["January", "February", "March", "April"])

#3->A Static dictionary of monthly sales:
#sales = {
 #   "January": 1200,
  #  "February": 1500,
   # "March": 900,
    #"April": 2000
#}
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

#4->Display selected month's sales using:
#st.matric() or st.write()
st.metric("total sales:",sales[months])

#Display a bar chart using:
#st.bar_chart(list(sales.vlaues()))
st.bar_chart(list(sales.values()))