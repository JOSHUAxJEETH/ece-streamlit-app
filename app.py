import streamlit as st
import random

st.set_page_config(page_title="ECE Department", layout="wide")

# Sidebar Navigation
st.sidebar.title("📡 ECE Portal")
menu = st.sidebar.radio("Navigation", ["Home", "About", "Labs", "Projects", "Live Data", "Contact"])

# Home Page
if menu == "Home":
    st.title("📡 Electronics & Communication Engineering")
    st.write("Welcome to the ECE Department Web Portal")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Vision")
        st.write("To innovate and lead in electronics and communication technologies.")

    with col2:
        st.subheader("Mission")
        st.write("To provide quality education and research opportunities.")

# About Page
elif menu == "About":
    st.title("🏫 About Department")
    st.write("""
    The ECE department focuses on:
    - Communication Systems
    - Embedded Systems
    - VLSI Design
    - Signal Processing
    """)

# Labs Page
elif menu == "Labs":
    st.title("🔬 Laboratories")
    st.write("• Analog Electronics Lab")
    st.write("• Digital Electronics Lab")
    st.write("• Communication Systems Lab")

# Projects Page
elif menu == "Projects":
    st.title("📁 Student Projects")
    st.write("• IoT Smart Monitoring System")
    st.write("• Wireless Sensor Network")
    st.write("• Edge AI Machine Monitoring")

# Live Data Page (Demo)
elif menu == "Live Data":
    st.title("📊 Live Sensor Dashboard")

    temp = random.randint(25, 40)
    voltage = random.uniform(3.0, 5.0)

    st.metric("Temperature", f"{temp} °C")
    st.metric("Voltage", f"{voltage:.2f} V")

# Contact Page
elif menu == "Contact":
    st.title("📞 Contact Us")

    name = st.text_input("Name")
    message = st.text_area("Message")

    if st.button("Submit"):
        st.success("Message sent successfully!")
