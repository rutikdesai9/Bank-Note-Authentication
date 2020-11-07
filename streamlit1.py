# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:54:01 2020

@author: Kishor
"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "The predicted value is "+str(prediction)



def main():
    st.title('Bank Authenticator')
    html_temp="""
    <div style="background-color:orange;padding:10px;">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML app</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("variance")
    skewness=st.text_input("skewness")
    curtosis=st.text_input("curtosis")
    entropy=st.text_input("entropy")
    result=" "
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button('About'):
        st.text('Made by Rutik Desai')
        

if __name__=='__main__':
    main()
