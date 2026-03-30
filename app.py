import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="ECE Dashboard", layout="wide")

# Sidebar
st.sidebar.title("📡 ECE Portal")
menu = st.sidebar.radio("Navigation", ["Home", "Live Data"])

# Home Page
if menu == "Home":
    st.title("📡 ECE Department")
    st.write("Sensor Monitoring Dashboard")

# Live Data Page
elif menu == "Live Data":
    st.title("📊 Enter Sensor Values")

    st.subheader("Enter Temperature Values (comma separated)")
    temp_input = st.text_input("Example: 25,30,28,35")

    st.subheader("Enter Voltage Values (comma separated)")
    volt_input = st.text_input("Example: 3.2,4.1,3.8,4.5")

    if st.button("Generate Graph"):

        try:
            temp_values = [float(x) for x in temp_input.split(",")]
            volt_values = [float(x) for x in volt_input.split(",")]

            df = pd.DataFrame({
                "Temperature": temp_values,
                "Voltage": volt_values
            })

            st.success("Graph Generated!")

            # ✅ SHOW TABLE
            st.subheader("📋 Data Table")
            st.dataframe(df)

            # 📈 Plot Graph
            fig, ax = plt.subplots()
            ax.plot(temp_values, label="Temperature")
            ax.plot(volt_values, label="Voltage")
            ax.set_title("Sensor Data Graph")
            ax.legend()

            st.pyplot(fig)

            # Save graph image
            fig.savefig("graph.png")

            # 📄 Create PDF
            doc = SimpleDocTemplate("report.pdf")
            styles = getSampleStyleSheet()

            content = []
            content.append(Paragraph("ECE Sensor Report", styles["Title"]))
            content.append(Spacer(1, 20))

            content.append(Paragraph(f"Temperature: {temp_values}", styles["Normal"]))
            content.append(Spacer(1, 10))

            content.append(Paragraph(f"Voltage: {volt_values}", styles["Normal"]))
            content.append(Spacer(1, 20))

            content.append(Image("graph.png", width=400, height=200))

            doc.build(content)

            # 📥 Download PDF
            with open("report.pdf", "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="report.pdf")

            # 📥 Download CSV
            st.download_button(
                "📥 Download Data CSV",
                df.to_csv(index=False),
                file_name="data.csv"
            )

        except:
            st.error("Please enter valid numbers separated by commas.")
