import streamlit as st
import pandas as pd

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
with st.form(key='Twitter_form'):
    search_term = st.text_input('User name')
    search_term = st.text_input('Date')
    limit = st.slider('How many tweets do you want to get?',0, 1000, step=20)
    submit_button = st.form_submit_button(label='Search')
             
