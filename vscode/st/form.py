import streamlit as st
import pandas as pd
from datetime import datetime

st.title("user information form")


form_values={
    'name':None,
    'gender':None,
    'dob':None,
    'age':None
}

min_date=datetime(1990,1,1)
max_date=datetime.now()

with st.form(key="user_information_form"):#السطر دا منغيره كل مره هتعدل في الفورم هيبقا لازم تعمل re run for the entire app
    form_values['name']=st.text_input("enter your name: ")

    form_values['gender']=st.selectbox("Gender",["male","female"] )
    birth_date=st.date_input("enter your birth date: ",max_value=max_date,min_value=min_date)
    if birth_date:
        age=max_date-birth_date.year

        if max_date.month<birth_date.month or (birth_date.month==max_date.month and birth_date.day >max_date.day):
            age-=1



    submit_button=st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("please fill in all of the fields")
    print(form_values)


