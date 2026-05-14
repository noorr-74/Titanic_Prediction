import streamlit as st
import os
#text elements:
st.title("يا مساء العكننه")
st.header("يحرق ابو الانسان على الصبح")
st.subheader("ليه بس كده")
st.markdown("يعم**انت مالك** بس")
st.caption("الصغير منه")

code_example=""""
def greet(name)
    print('hello',name)

    """
st.code(code_example,language="python")

st.subheader("القاسم ")
st.divider()

st.image(os.path.join(os.getcwd(),"static","download.jpeg"),width=500,)#get the currnet working directory
#os.path.join:join diffrent paths