import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.write("Data Dashboard")
# st.write({
#     "key": "some_value",
#     "key2" : "some_other_value",

# })

st.title("Simple data dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("data Preview")
    st.write(df.head())


    st.subheader("Data Summary")
    st.write(df.describe())


    st.subheader("Filter Data")

    columns = df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by", columns)

    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    st.write(filtered_df)

    st.subheader("Plot data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("waiting for file upload...")
