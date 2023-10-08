import streamlit as st
import pandas as pd
import numpy as np
st.title("Demo Calculator")
st.header("Enter inputs to calculate")
st.sidebar.image("")


col1, col2 = st.columns([1,1])
with col1:
    n1 = st.text_input("Enter first number", value=0)

with col2:
    n2 = st.text_input("Enter second number", value=0)

operator = st.selectbox("Select Operator", ['+', '-', '*', '/'])
n1 = float(n1)
n2 = float(n2)
if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    result = n1 / n2

c1, c2, c3 = st.columns([1, 1, 1])

with c2:
    btn = st.button('Calculate')


if btn:
    st.success(f'The result  is {result}.')