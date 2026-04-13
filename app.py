import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Power Quality Analyzer", layout="wide")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Theory", "Principle", "Analysis", "Report", "Quiz", "Feedback"]
)

# ---------------- SESSION ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Voltage", "Current", "Frequency", "Power Factor", "Power"
    ])

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.title("⚡ Smart Power Quality Analyzer")
    st.subheader("Interactive Learning & Analysis System")

    st.markdown("""
    ### 🎯 Welcome

    This system helps users:
    - Learn power quality concepts 📘  
    - Input electrical parameters ⚡  
    - Analyze system performance 📊  
    - Generate reports 📄  

    👉 Use the sidebar to explore all features.
    """)

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.title("📘 Theory")

    st.write("""
    Power quality refers to maintaining stable voltage, current, and frequency.

    Poor power quality may lead to:
    - Equipment damage  
    - Power loss  
    - Reduced efficiency  

    Key Parameters:
    - Voltage (V)
    - Current (A)
    - Frequency (Hz)
    - Power Factor
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.title("⚙️ Working Principle")

    st.write("""
    1. User enters electrical parameters  
    2. System calculates power using:  
       Power = Voltage × Current × Power Factor  
    3. Data is stored  
    4. Graph shows variation  
    5. Alerts detect abnormal conditions  
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

    # ALERT
    if power > 2000:
        st.error("🔴 Overload Condition")
    elif power > 1000:
        st.warning("🟠 High Load")
    else:
        st.success("🟢 Normal Condition")

# ---------------- REPORT ----------------
elif menu == "Report":
    st.title("📄 Report Download")

    if not st.session_state.data.empty:
        st.download_button(
            "Download CSV",
            st.session_state.data.to_csv(index=False),
            "power_report.csv"
        )
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
