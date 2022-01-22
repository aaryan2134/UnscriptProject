import streamlit as st
import pickle
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
from bokeh.models.widgets import Div
import streamlit as st



def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def main():

     local_css("style.css")
     #
     # t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"
     #
     # st.markdown(t, unsafe_allow_html=True)

     st.markdown("<h1 style='text-align: center; color: black;'>FUNANCO</h1>", unsafe_allow_html=True)
     st.markdown("<h1 style='text-align: center; color: black; font-size: 25px;'>(User-Friendly Financial Database)</h1>", unsafe_allow_html=True)


     df = pd.read_csv("AIML Dataset.csv")

     TRANSACTION_ID = st.text_input("ENTER TRANSACTION ID:")
     
     if(TRANSACTION_ID):
         temp = df.loc[df['nameOrig'] == TRANSACTION_ID]
         amt = np.array(temp.amount)
         type = np.array(temp.type)
         oldBalanceOrig = np.array(temp.oldbalanceOrg)
         newBalanceOrig = np.array(temp.newbalanceOrig)
         nameDest = np.array(temp.nameDest)


         st.write("Amount: {}".format(amt[0]))
         #st.write(amt[0])
         st.write("Type: {}".format(type[0]))
         #st.write(type[0])
         st.write("User's Old Balance: INR {}".format(oldBalanceOrig[0]))
         #st.write(oldBalanceOrig[0])
         st.write("User's New balance: INR {}".format(newBalanceOrig[0]))
         #st.write(newBalanceOrig[0])

         # df_temp = pd.DataFrame({'Amount (INR)': amt[0], ' Type of Transaction': type[0], "User's Old Balance (INR)": oldBalanceOrig[0], "User's New balance (INR)": newBalanceOrig[0]}, index = ["Values: "])
         # st.dataframe(df_temp)


         if(temp.isFraud.to_numpy()[0]==1):
             st.write("FRAUD DETECTED")

         if(temp.isFraud.to_numpy()[0]==0):
             st.write("NO FRAUD DETECTED")

         url = "https://jprfg.csb.app/"
         st.markdown("[Homepage](%s)" % url)



         #st.markdown("check out this [link](%s)" % url)
         #     # js = "window.open('https://www.streamlit.io/')"  # New tab or window
         #     js = "window.location.href = 'https://jprfg.csb.app/'"  # Current tab
         #     html = '<img src onerror="{}">'.format(js)
         #     div = Div(text=html)
         #     st.bokeh_chart(div)
       
     
     
if __name__ == '__main__':
     	main()     