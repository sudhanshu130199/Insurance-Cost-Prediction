import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Insurance Premium Estimator')


df = pd.read_csv("insurance.csv")

st.dataframe(df)




age = st.slider("Age",18,66)

col1, col2 = st.columns(2)

diabetes = col1.selectbox('Diabetes', ['No', 'Yes'])
blood_pressure = col1.selectbox('Blood Pressure Problems', ['No', 'Yes'])
transplants = col2.selectbox('Any Transplants', ['No', 'Yes'])
chronic_diseases = col2.selectbox('Any Chronic Diseases', ['No', 'Yes'])

col1, col2 = st.columns(2)
height = col1.slider('Height (cm)', 145, 188)
weight = col1.slider('Weight (kg)', 51, 132)
allergies = col2.selectbox('Known Allergies', ['No', 'Yes'])
cancer_history = col2.selectbox('History of Cancer in Family', ['No', 'Yes'])

col1, col2 = st.columns(2)
surgeries = col1.slider('Number of Major Surgeries', 0, 3)
bmi = col2.slider('BMI', 15,50)







input_data = pd.DataFrame({
    'Age': [age],
    'Diabetes': [1 if diabetes == 'Yes' else 0],
    'BloodPressureProblems': [1 if blood_pressure == 'Yes' else 0],
    'AnyTransplants': [1 if transplants == 'Yes' else 0],
    'AnyChronicDiseases': [1 if chronic_diseases == 'Yes' else 0],
    'Height': [height],
    'Weight': [weight],
    
    'KnownAllergies': [1 if allergies == 'Yes' else 0],
    'HistoryOfCancerInFamily': [1 if cancer_history == 'Yes' else 0],
    'NumberOfMajorSurgeries': [surgeries],
    'BMI': [bmi]
})

if st.button('Estimate Premium'):
    try:
        prediction = model.predict(input_data)
        st.write(f'Estimated Premium: ₹{prediction[0]:.2f}')  # Format with currency
    except Exception as e:
        st.error(f'An error occurred: {e}')