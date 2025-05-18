import streamlit as st
from HospitalManagementSystem import main as hms_main

st.title("Hospital Management System")
if st.button("View Doctors"):
    # Здесь вызовите ваш метод view_doctors()
    st.write("Список врачей...")