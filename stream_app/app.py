import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world")
fav_movie = st.text_area("favourite movie?")

st.write("Your favourite movie is", fav_movie)

st.write("## H2 heading via markdown")

data = pd.read_csv("../car_sales.csv")

st.write(data)


chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns =["a", "b", "c"]
)

st.bar_chart(chart_data)

st.line_chart(chart_data)

st.link_button("Profile", "/pages/profile")