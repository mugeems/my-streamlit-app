import streamlit as st
import pandas as pd

st.title('My Simple Streamlit App')

st.write('Hello, World!')

# Create sample data
data = {
    'Name': ['John', 'Jane', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

# Display the dataframe
st.dataframe(df)

# Add a simple widget
name = st.text_input('Enter your name')
if name:
    st.write(f'Hello, {name}!')
