#Task-1:Basic Streamlit App(app_basic.py)
#Create a basic Streamlit app that:
#use:
#st.title()
#st.text_input()
#st.button()
#st.write()

#1->Displays a title: "Welcome to Streamlit!"
import streamlit as st
st.title("Welcome to Streamlit!")

#2->show a text input box for entering you name.
st.text_input("name:")

#3->When user clicks a button "Greet Me", display
# "Hello,!"
if st.button("Greet Me"):
    st.write("Hello,!")

