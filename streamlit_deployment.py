
# from turtle import color
# import streamlit as st
# import pandas as pd
# import numpy as np
# import streamlit.components.v1 as components

# def main():
  
#   df = pd.read_csv('AIML Dataset.csv')
#   user = st.text_input("Enter the TRANSACTION ID: ")
#   # Select rows where sample_col1 is 1
#   temp = df.loc[df['nameOrig'] == user]
#   st.write(temp.amount)
#   st.write(temp.newbalanceOrig)
#   st.write(temp.type)
#   st.write(temp.step)
#   st.write(temp.nameOrig)
#   tp= st.write(temp.isFraud)
#   tn='''<html><body><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><h1 class="red-700">This is a Fraud Transaction</h1></body></html>'''
#   tj='''<html><body><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><h1 class="red-700">This is not a Fraud Transaction</h1></body></html>'''
#   if(temp.isFraud.to_numpy()[0]==1):
#       components.html(tn,width=500,height=100)
#   if(temp.isFraud.to_numpy()[0]==0):
#            components.html(tj,width=500,height=100)

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
def main():
     df = pd.read_csv("AIML Dataset.csv")


     TRANSACTION_ID = st.text_input("ENTER TRANSACTION ID:")
     
     if(TRANSACTION_ID):
         temp = df.loc[df['nameOrig'] == TRANSACTION_ID]
         amt = np.array(temp.amount)
         type = np.array(temp.type)
         oldBalanceOrig = np.array(temp.oldbalanceOrg)
         newBalanceOrig = np.array(temp.newbalanceOrig)
         nameDest = np.array(temp.nameDest)
         st.write(amt[0])
         st.write(type[0])
         st.write(oldBalanceOrig[0])
         st.write(newBalanceOrig[0])
         tn='''<html><body><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><h1 class="red-700">This is a Fraud Transaction</h1></body></html>'''
         tj='''<html><body><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><h1 class="red-700">This is not a Fraud Transaction</h1></body></html>'''
         if(temp.isFraud.to_numpy()[0]==1):
              components.html(tn,width=500,height=100)
         if(temp.isFraud.to_numpy()[0]==0):
              components.html(tj,width=500,height=100)     
       
     
     
if __name__ == '__main__':
     	main()     