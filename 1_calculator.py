import streamlit as st

st.title('Simple Calculator')

num1 = st.number_input('First num',min_value=0,step=1,format='%d')
num2 = st.number_input('Second num',min_value=0,step=1,format='%d')
ops = st.radio("select:",['Add','Subtract','Multiply','Divide'])

if st.button('calulate'):
    if ops == 'Add':
        st.success(f"Result: {num1+num2}")
    elif ops == 'Subtract':
        st.success(f"Result: {num1-num2}")
    elif ops == 'Multiply':
        st.success(f"Result: {num1*num2}")
    elif ops == 'Divide':
        if num2 == 0:
            st.write('Cannot divide by zero')
        else:
            st.success(f"Result: {num1/num2}")
