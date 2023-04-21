# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:25:21 2023

@author: alok
"""

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("Navigation",['About','Predict'])
df = pd.read_csv("insurance.csv")

if nav=="About":
    st.title("Health Insurance Premium Predictor")
    st.text("")
    st.text("")
    st.image("Health-Lead.jpg")


## feature encoding    
df.replace({'sex':{'male':0,'female':1}}, inplace=True)
df.replace({'smoker':{'yes':0,'no':1}}, inplace=True)
df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

x=df.drop(columns='expenses',axis=1)
y= df['expenses']

rfr= RandomForestRegressor()
rfr.fit(x,y)

if nav=='Predict':
    st.title("Enter Details")
    age=st.number_input("Age",step=1,min_value=0)
    sex=st.radio("Sex",('Male','Female'))
    
    if(sex=="Male"):
        s=0
    if(sex=='Female'):
        s=1
    bmi= st.number_input(("BMI"))
    children= st.number_input("Number of Children:",step=1, min_value=0)
    smoke= st.radio("Do you smoke", ('yes','no'))
    if (smoke=='yes'):
        sm=0
    if (smoke=='no'):
        sm=1
        
        
    region= st.selectbox('Region',('southeast','southwest','northeast','northwest'))
    if (region=='southeast'):
        reg=0
    if (region=='southwest'):
        reg=1
    if (region=='northeast'):
        reg=2
    if (region=='northwest'):
        reg=3
        
    if st.button("Predict"):
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age,s,bmi,children,sm,reg]]))