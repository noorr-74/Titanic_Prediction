import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter=0

if st.button("Increment Counter"):
    st.session_state.counter+=1
    st.write(f"counter incremenet to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter =0
else:
    st.write("counter did not reset")

st.write(f"counter vlaue:{st.session_state.counter}")


