import streamlit as st

st.write("Hello")

st.header('st.selectbox')

option = st.selectbox(
     'Menu',
     ('About', 'Search', 'Upload', 'Download'))

st.write(option)
