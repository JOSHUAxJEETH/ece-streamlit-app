import streamlit as st
import pandas as pd
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Power Quality Analyzer", layout="wide")

# ---------------- SESSION ----------------
if "registered" not in st.session_state:
    st.session_state.registered = False

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Voltage", "Current", "Frequency", "Power Factor", "Power"
    ])

# ---------------- REGISTRATION ----------------
if not st.session_state.registered:
    st.title("📝 Registration")

    name = st.text_input("Enter Name")
    reg = st.text_input("Register Number")

    if st.button("Register"):
        if name and reg:
            st.session_state.registered = True
            st.session_state.name = name
            st.session_state.reg = reg
            st.success("Registered Successfully ✅")
        else:
            st.error("Please fill all details")

    st.stop()

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Theory", "Principle", "Analysis", "Report", "Quiz", "Feedback"]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.title("⚡ Smart Power Quality Analyzer")
    st.subheader("Interactive Learning & Analysis System")

    st.markdown(f"""
    👤 **User:** {st.session_state.name}  
    🆔 **Register No:** {st.session_state.reg}

    ---

    ### 🎯 Welcome

    This system helps you:
    - Learn power quality concepts 📘  
    - Input electrical parameters ⚡  
    - Analyze system performance 📊  
    - Generate PDF report 📄  

    👉 Use the sidebar to navigate.
    """)

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.title("📘 Theory")

    st.write("""
    Power quality refers to maintaining stable voltage, current, and frequency.

    Poor power quality leads to:
    - Equipment damage  
    - Energy loss  
    - Reduced efficiency  

    Key parameters:
    - Voltage (V)
    - Current (A)
    - Frequency (Hz)
    - Power Factor
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.title("⚙️ Working Principle")

    st.write("""
    1. User inputs electrical parameters  
    2. System calculates power  
    3. Data stored in table  
    4. Graph visualizes variation  
    """)

# ---------------- ANALYSIS ----------------
elif menu == "Analysis":
    st.title("📊 Power Analysis")

    st.subheader("Enter Values")

    col1, col2 = st.columns(2)

    with col1:
        voltage = st.number_input("Voltage (V)", 0, 500)
        current = st.number_input("Current (A)", 0, 50)

    with col2:
        frequency = st.number_input("Frequency (Hz)", 0, 100)
        pf = st.number_input("Power Factor", 0.0, 1.0)

    power = voltage * current * pf

    if st.button("Add Row"):
        new_row = {
            "Voltage": voltage,
            "Current": current,
            "Frequency": frequency,
            "Power Factor": pf,
            "Power": power
        }

        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([new_row])],
            ignore_index=True
        )

    # TABLE
    st.subheader("📋 Data Table")
    st.dataframe(st.session_state.data)

    # GRAPH
    if not st.session_state.data.empty:
        st.subheader("📈 Power Graph")
        st.line_chart(st.session_state.data["Power"])

# ---------------- REPORT (PDF) ----------------
elif menu == "Report":
    st.title("📄 Download PDF Report")

    if not st.session_state.data.empty:

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Power Quality Report", ln=True)
        pdf.cell(200, 10, txt=f"Name: {st.session_state.name}", ln=True)
        pdf.cell(200, 10, txt=f"Register No: {st.session_state.reg}", ln=True)
        pdf.ln(5)

        for i, row in st.session_state.data.iterrows():
            text = f"{i+1}. V={row['Voltage']} I={row['Current']} F={row['Frequency']} PF={row['Power Factor']} P={row['Power']}"
            pdf.cell(200, 10, txt=text, ln=True)

        pdf.output("report.pdf")

        with open("report.pdf", "rb") as f:
            st.download_button("Download PDF", f, "Power_Report.pdf")

    else:
        st.warning("No data available")

# ---------------- QUIZ ----------------
elif menu == "Quiz":
    st.title("🧠 Quiz")

    score = 0

    q1 = st.radio("Power formula?", ["V + I", "V × I × PF", "I / V"])

    if st.button("Submit"):
        if q1 == "V × I × PF":
            score += 1

        st.success(f"Score: {score}/1")

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.title("📝 Feedback")

    fb = st.text_area("Enter feedback")

    if st.button("Submit"):
        st.success("Feedback submitted successfully!")
