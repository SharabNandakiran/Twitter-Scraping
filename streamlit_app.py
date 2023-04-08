import streamlit as st
import pandas as pd

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
with st.form(key='Twitter_form):
    search_term = st.text_input('User name')
             
