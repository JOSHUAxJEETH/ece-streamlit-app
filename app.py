import streamlit as st
import pandas as pd
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Power Quality Analyzer", layout="wide")

# ---------------- TITLE ----------------
st.title("⚡ Smart Power Quality Analyzer")
st.subheader("Interactive Learning & Analysis System")

# ---------------- SESSION ----------------
if "registered" not in st.session_state:
    st.session_state.registered = False

if "data" not in st.session_state:
    st.session_state.data = []

# ---------------- REGISTRATION ----------------
if not st.session_state.registered:
    st.header("📝 Registration")

    name = st.text_input("Enter Name")
    reg = st.text_input("Register Number")

    if st.button("Register"):
        if name and reg:
            st.session_state.registered = True
            st.session_state.name = name
            st.session_state.reg = reg
            st.success("Registered Successfully ✅")
        else:
            st.error("Fill all details")

    st.stop()

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Theory", "Principle", "Analysis", "Report", "Quiz", "Feedback"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("🎯 Aim")

    st.write("""
    To analyze power quality parameters such as voltage and current
    and understand their effect on electrical systems.
    """)

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.header("📘 Theory")

    st.write("""
    Power quality refers to the stability and consistency of voltage and current.
    
    Poor power quality can cause:
    - Equipment damage
    - Power losses
    - System inefficiency
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.header("⚙️ Working Principle")

    st.write("""
    1. User inputs voltage and current  
    2. System calculates power (P = V × I)  
    3. Graph shows variation  
    4. Helps analyze system performance  
    """)

# ---------------- ANALYSIS ----------------
elif menu == "Analysis":
    st.header("📈 Power Analysis")

    col1, col2 = st.columns(2)

    with col1:
        voltage = st.number_input("Enter Voltage (V)", 0, 500)
        current = st.number_input("Enter Current (A)", 0, 50)

        if st.button("Add Data"):
            power = voltage * current
            st.session_state.data.append(power)

    with col2:
        st.write("Power = Voltage × Current")

    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data, columns=["Power"])
        st.line_chart(df)

# ---------------- REPORT ----------------
elif menu == "Report":
    st.header("📄 Download Report")

    if st.session_state.data:

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Power Quality Report", ln=True)

        for i, val in enumerate(st.session_state.data):
            pdf.cell(200, 10, txt=f"Reading {i+1}: {val} W", ln=True)

        pdf.output("report.pdf")

        with open("report.pdf", "rb") as f:
            st.download_button("Download PDF", f, "report.pdf")

    else:
        st.warning("No data available")

# ---------------- QUIZ ----------------
elif menu == "Quiz":
    st.header("🧠 Quiz")

    score = 0

    q1 = st.radio("Power formula?", ["V + I", "V × I", "I / V"])

    if st.button("Submit"):
        if q1 == "V × I":
            score += 1

        st.success(f"Score: {score}/1")

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.header("📝 Feedback")

    fb = st.text_area("Enter feedback")

    if st.button("Submit"):
        st.success("Thanks for feedback!")
