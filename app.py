elif menu == "Live Data":
    st.title("📊 Sensor Data Dashboard")

    import random
    import pandas as pd

    # Generate random data
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

    st.subheader("Data Table")
    st.dataframe(df)
