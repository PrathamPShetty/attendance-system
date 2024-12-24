import streamlit as st

st.title("Contact Us")
icons=["envelope"]

if "my_input" not in st.session_state:
    st.session_state["my_input"]=""

if "my_input1" not in st.session_state:
    st.session_state["my_input1"]=""

my_input=st.text_input("Enter your email:",st.session_state["my_input"])

my_input1=st.text_input("Enter the summary of your problem:",st.session_state["my_input1"])
submit=st.button("Submit")

if submit:
    st.session_state["my_input"]=my_input
    st.session_state["my_input1"]=my_input1
    st.write("We'll reach you out soon")

