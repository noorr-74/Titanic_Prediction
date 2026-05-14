import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#genrate sample data
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

#Area chart
st.subheader("areea chart")
st.area_chart(chart_data)

#Bar chart
st.subheader("Bar chart")
st.bar_chart(chart_data)

#Line chart
st.subheader("line chart")
st.line_chart(chart_data)


#scatter plot
st.subheader("scatter plot")
st.scatter_chart(chart_data)
