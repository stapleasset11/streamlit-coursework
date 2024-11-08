import streamlit as st

st.title("Lesson 04: Session State.")

if "counter" not in st.session_state:
    st.session_state.counter = 0


if st.button("up"):
    st.write(st.session_state.counter)
    st.session_state.counter += 1
    


if st.button("Reset"):
    st.session_state.counter = 0

