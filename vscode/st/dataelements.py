import streamlit as st
import pandas as pd


st.title("streamlit demo")
#data framest.
st.subheader("Data Frame")
df=pd.DataFrame({
    'Name':['Alice','Bob','yousef','joex'],
    'Age':[20,22,24,29],
    'ocuupation ':['Eng','Dr','Artist','player']
    
})
st.dataframe(df)
#data editor section
st.subheader("Data Frame Editor")
edited=st.data_editor(df)
print(edited)

#static table
st.subheader("static table")
st.table(df)

#Metrics Section
st.subheader("Static Table")
st.metric(label="rows",value=len(df))
st.metric(label="average age",value=round(df['Age'].mean(),1))#round used to round the number after point to only one digit



