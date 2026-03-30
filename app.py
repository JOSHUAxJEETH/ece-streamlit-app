import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="ECE Department", layout="wide")

# Sidebar
st.sidebar.title("📡 ECE Portal")
menu = st.sidebar.radio("Navigation", ["Home", "About", "Labs", "Projects", "Live Data", "Contact"])

# Home
if menu == "Home":
    st.title("📡 Electronics & Communication Engineering")
    st.write("Welcome to the ECE Department Web Portal")

# About
elif menu == "About":
    st.title("🏫 About Department")
    st.write("""
    - Communication Systems
    - Embedded Systems
    - VLSI Design
    - Signal Processing
    """)

# Labs
elif menu == "Labs":
    st.title("🔬 Laboratories")
    st.write("• Analog Lab")
    st.write("• Digital Lab")

# Projects
elif menu == "Projects":
    st.title("📁 Projects")
    st.write("• IoT Monitoring System")

# ✅ Correct Live Data Section
elif menu == "Live Data":
    st.title("📊 Sensor Dashboard")

    data = {
        "Time": list(range(1, 21)),
        "Temperature": [random.randint(25, 40) for _ in range(20)],
        "Voltage": [round(random.uniform(3.0, 5.0), 2) for _ in range(20)]
    }

    df = pd.DataFrame(data)

    st.subheader("Temperature Graph")
    st.line_chart(df["Temperature"])

    st.subheader("Voltage Graph")
    st.line_chart(df["Voltage"])

    st.dataframe(df)

# Contact
elif menu == "Contact":
    st.title("📞 Contact")
    st.write("Email: ece@example.com")
