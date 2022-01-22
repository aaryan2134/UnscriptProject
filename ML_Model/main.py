import sklearn
import joblib
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

model = joblib.load('model.pkl')

st.markdown("<h1 style='text-align: center; color: black;'>FRAUD-DETECTION</h1>", unsafe_allow_html=True)

step = st.text_input("Enter Step value: ")
amount = st.text_input("Enter Amount transacted: ")
newBalorg = st.text_input("Enter New Balance: ")
newBalDest = st.text_input("Enter Destination Account's new Balance: ")

option = st.selectbox('Select the type of transaction ? ', ('CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'))

if(option == "CASH_OUT"):
    CASH_OUT = 1
    debit = 0
    payment = 0
    transfer = 0
if(option == "DEBIT"):
    CASH_OUT = 0
    debit = 1
    payment = 0
    transfer = 0
if(option == "PAYMENT"):
    CASH_OUT = 0
    debit = 0
    payment = 1
    transfer = 0
if(option == "TRANSFER"):
    CASH_OUT = 0
    debit = 0
    payment = 0
    transfer = 1

if st.button("Predict!"):
    inp = pd.DataFrame({"step": step, "amount": amount,  'newBalanceOrig': newBalorg, 'newBalanceDest': newBalDest, "CASH_OUT": CASH_OUT, "DEBIT":debit, "PAYMENT":payment, "TRANSFER":transfer}, index = [0])

    if(model.predict(inp)[0]==0):
        st.write("NO FRAUD DETECTED")
    else:
        st.write("FRAUD DETECTED")


url = "https://jprfg.csb.app/"
st.markdown("[Homepage](%s)" % url)


