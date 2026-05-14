import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("simple Data Dashbord")

upload_file=st.file_uploader("choose a csv file",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)

    st.subheader("data preview")
    st.write(df)

    st.subheader("data summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns=df.columns.tolist()
    selected_column=st.selectbox("select cloumn to filter by",columns)

    unique_values=df[selected_column].unique()
    selected_value=st.selectbox("select value",unique_values)

    filtered_df=df[df[selected_column]==selected_value]
    st.subheader("filtered pclass")
    st.write(filtered_df)

    st.subheader("plot data")
    x_cloumn=st.selectbox("select x-axis cloumn",columns)
    y_cloumn=st.selectbox("select y-axis cloumn",columns)

    if st.button("generate plot"):
        st.line_chart(filtered_df.set_index(x_cloumn)[y_cloumn])
else:
    st.write("wainting for file uploaded ")
