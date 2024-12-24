import streamlit as st
import pandas as pd
from attendence import start_attendance_system

# Page Config
st.set_page_config(
    page_title="Smart Attendance System",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Take Attendance", "View Attendance", "Contact Us"])

# Home Page
if page == "Home":
    st.title("Welcome to Smart Attendance System")
    st.write("""
    The Smart Attendance System Using Face Recognition streamlines attendance tracking with facial recognition technology. 
    It ensures accurate, proxy-free, and secure attendance management.
    """)

# Take Attendance Page
elif page == "Take Attendance":
    st.title("Take Attendance 📷")
    if st.button("Start Webcam Attendance"):
        start_attendance_system()
    st.success("Attendance session completed. Check 'View Attendance' for details.")

# View Attendance Page
elif page == "View Attendance":
    st.title("Attendance Records 📊")
    try:
        df = pd.read_csv("Attendance.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("No attendance records found. Start attendance first!")

# Contact Us Page
elif page == "Contact Us":
    st.title("Contact Us 📧")
    if "email" not in st.session_state:
        st.session_state["email"] = ""
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    email = st.text_input("Enter your email:", st.session_state["email"])
    summary = st.text_area("Enter the summary of your problem:", st.session_state["summary"])
    submit = st.button("Submit")

    if submit:
        st.session_state["email"] = email
        st.session_state["summary"] = summary
        st.success("We'll reach out to you soon!")
