import streamlit as st

with st.expander("Expander with scrolling content"):
    with st.container(height=200):
        st.write("Inside scrolling container")
