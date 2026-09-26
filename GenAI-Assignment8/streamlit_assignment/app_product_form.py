#Task->3: Product From(app_product_from.py)
#Creat a simple form UI
#use components:
#st.sidebar.text_input
#st.sidebar.selectbox
#st.sidebar.numbe_input
#st.sidebar.button

#1->Use Streamlit sidebar to enter:
#Product Name
import streamlit as st
product_name = st.sidebar.text_input("Product Name:")

#Category(selectbox with 3-5 options)
Category = st.sidebar.selectbox("Category:",["Electronics", "Clothing", "Food", "Books"])

#price 
Price = st.sidebar.number_input("price:",min_value=0)

#when user clicks "Add Product", show:
#A Success message
#the Product details in clean format
button = st.sidebar.button("Add Product")
if button:
    st.success("Product details added successfully!")
    st.write("product Details")
    st.write("product name:", product_name)
    st.write("category:", Category)
    st.write("Price:", Price)
