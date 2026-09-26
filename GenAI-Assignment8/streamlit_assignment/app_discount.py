#Build a simple price calcualtor app that:

#1->Takes product price(number input)
import streamlit as st
Price = st.number_input("Enter number:",min_value=0,step=1)
st.write("the price accepts only positive values only")

#2->Takes discount percentage(slider from 0 to 50%)
discount_percentage = st.slider("select discount percentage:", 0, 10, 50)
st.write(f"selected percentage:{discount_percentage}") 

#3->on button click, calculates discounted price
if st.button("discounted price"):
    discount_amount = Price * discount_percentage/ 100
    final_price = Price - discount_amount
    st.success("Discount calculated successfully!")
    st.write(f"Price After discount:{final_price}")

    #Extra(optional): show comparison in a small table:
    #before | After
    #(use st.table() with s aimple list of lists)
    st.table([
        ["Before", "After"],
        [Price, final_price]
    ])
#Example:
#Original Price: 1000
#Discount: 10%
#Final Price: 900