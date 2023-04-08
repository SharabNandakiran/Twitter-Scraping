import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


st.header('st.write')

st.write('Hello,*world!* : sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    })
st.write(df)
  
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
  
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c',tooltip=['a','b','c'])
st.write(c)


st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)
