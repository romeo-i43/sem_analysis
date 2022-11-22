import streamlit as st
import pandas as pd
import plotly_express as px

def app():
    hide_st_style1 = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style1, unsafe_allow_html=True)
    hide_st_style = """
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.title('ploty')
    st.subheader('table')
    st.markdown('<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>',unsafe_allow_html=True)
    st.markdown('---')
    sem=st.radio("select the semester",["1stsem1","1stsem2","2ndsem1","2ndsem2"])
    if sem=="1stsem1":
        df=pd.read_csv('./1stsem1.csv')
    elif sem =="1stsem2":
        df=pd.read_csv('./1stsem2.csv')
    elif sem=="2ndsem1":
        df=pd.read_csv('./2ndsem1.csv')
    elif sem=="2ndsem2":
        df=pd.read_csv('./2ndsem2.csv')
    st.dataframe(df)
