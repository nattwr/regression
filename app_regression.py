import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('pipeline_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Import Value Prediction App')

# Input fields for user to enter data
weight = st.number_input('Enter weight (น้ำหนัก สถิติ):')
volume = st.number_input('Enter volume (ปริมาณ สถิติ):')
unit = st.selectbox('Select unit (หน่วยปริมาณ):', ['BG','KGM','LO','SA','TNE','CT','C62','PK','BX','SH','PA'])  # Replace with actual units

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'น้ำหนัก สถิติ': [weight],
    'ปริมาณ สถิติ': [volume],
    'หน่วยปริมาณ': [unit]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Import Value (มูลค่านำเข้าเงินบาท): {prediction[0]}')
