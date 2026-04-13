import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Power Quality Analyzer", layout="wide")

# ---------------- TITLE ----------------
st.title("⚡ Smart Power Quality Analyzer")
st.subheader("Advanced Interactive Learning & Analysis System")

# ---------------- SESSION ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Voltage", "Current", "Power", "Frequency", "Power Factor"
    ])

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Theory", "Principle", "Report", "Quiz", "Feedback"]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.header("📊 Real-Time Power Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        voltage = st.slider("Voltage (V)", 0, 500, 230)

    with col2:
        current = st.slider("Current (A)", 0, 50, 10)

    with col3:
        frequency = st.slider("Frequency (Hz)", 45, 65, 50)

    power_factor = st.slider("Power Factor", 0.0, 1.0, 0.9)

    # AUTO CALCULATE
    power = voltage * current * power_factor

    # AUTO ADD BUTTON
    if st.button("➕ Add Reading"):
        new_row = {
            "Voltage": voltage,
            "Current": current,
            "Power": power,
            "Frequency": frequency,
            "Power Factor": power_factor
        }
        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([new_row])],
            ignore_index=True
        )

    # ---------------- METRICS (GAUGE STYLE) ----------------
    st.subheader("⚡ Live Metrics")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Voltage", f"{voltage} V")

    with m2:
        st.metric("Current", f"{current} A")

    with m3:
        st.metric("Power", f"{power:.2f} W")

    # ---------------- ALERT SYSTEM ----------------
    if voltage > 260 or power > 2000:
        st.error("🔴 Danger: Overload Condition!")
    elif voltage > 240:
        st.warning("🟠 Warning: High Voltage")
    else:
        st.success("🟢 System Stable")

    # ---------------- TABLE ----------------
    st.subheader("📋 Data Table")
    st.dataframe(st.session_state.data)

    # ---------------- GRAPH ----------------
    st.subheader("📈 Power Trend Graph")

    if not st.session_state.data.empty:
        st.line_chart(st.session_state.data["Power"])

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.header("📘 Theory")

    st.write("""
    Power Quality refers to maintaining voltage, current, frequency within limits.

    Key parameters:
    - Voltage stability
    - Current flow
    - Frequency
    - Power factor

    Poor power quality can damage equipment.
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.header("⚙️ Working Principle")

    st.write("""
    1. Measure voltage, current, frequency  
    2. Calculate power using formula  
    3. Detect abnormal conditions  
    4. Alert user  
    """)

# ---------------- REPORT ----------------
elif menu == "Report":
    st.header("📄 Data Report")

    if not st.session_state.data.empty:
        st.download_button(
            "Download CSV",
            st.session_state.data.to_csv(index=False),
            "report.csv"
        )
    else:
        st.warning("No data available")

# ---------------- QUIZ ----------------
elif menu == "Quiz":
    st.header("🧠 Quiz")

    score = 0

    q1 = st.radio("Power formula?", ["V + I", "V × I × PF", "I / V"])

    if st.button("Submit"):
        if q1 == "V × I × PF":
            score += 1

        st.success(f"Score: {score}/1")

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.header("📝 Feedback")

    fb = st.text_area("Enter feedback")

    if st.button("Submit"):
        st.success("Feedback submitted!")
