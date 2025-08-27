import streamlit as st 
import pandas as pd
import numpy as np

#Title of application
st.title("Hello streamlit")

#Display simple text
st.write("This is a simple text")

#Create and showing simple data Frame
df = pd.DataFrame({
    'First Column' : [1,2,3,4],
    'second Column': [10, 20, 30, 40]
})
st.write("Here is the data frame")
st.write(df)


#Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=('a', 'b', 'c')
) 
st.line_chart(chart_data)