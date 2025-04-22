import streamlit as st  
import pandas as pd 
import pickle

def classify(age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal):

    with open('./models/Model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('./models/scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    
    return model.predict(scaler.transform([[age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal]]))




st.title("Classification of Heart Disease")
st.write("Enter your report details here....")


age = st.number_input("Enter your age: ", )

st.write("Sex types:")
st.write("0 Female \n1 Male")
sex = st.number_input("Enter your sex:", )

st.write("Chest pain types:")
st.write("1. Typical angina \n2. Atypical angina\n 3. Non-anginal pain\n 4. Asymptomatic")
cp = st.number_input("Enter the chest pain type: ", )

trestbps = st.number_input("Enter your blood pressure rate (mm/Hg): ", )

chol = st.number_input("Enter your total cholesterol level (mg/dl): ", )

st.write("Resting electrocardiographic results")
st.write("1. 0 for Normal\n2. 1 for Having ST-T wave abnormality (indicating possible heart attack) or Hypertrophy of the left ventricle (enlarged heart)")
restecg = st.number_input("Enter your Resting electrocardiographic results: ", )

thalach = st.number_input("Enter your maximum heart rate achieved: ", )

st.write("Exercise-induced angina notation:")
st.write("1. 1 for Yes \n2. 0 for No")
exang = st.number_input("Enter your exercise-induced angina", )

oldpeak = st.number_input("Enter your oldpeak value:", )

st.write("Slope: ST segment slope at peak exercise notation:")
st.write("1. Upsloping \n2. Flat \n3. Downsloping")
slope = st.number_input("Enter your slope value: ", )

ca = st.number_input("Enter your ca(Number of coronary arteries with significant stenosis (blockage)) value: ", )

st.write("Thalassemia notation:")
st.write("1. Normal \n2. Fixed defect \n3. Reversible defect")
thal = st.number_input("Enter your thal value:", )

if st.button("Predict"):
    if classify(age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal) == 0:
        st.write("Hey, You are fit...")
    else:
        st.write("You need treatment...")    
