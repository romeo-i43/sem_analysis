import streamlit as st
import pandas as pd
import plotly_express as px
import time
from streamlit_lottie import st_lottie
import requests

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

    st.title("plot based on your requirement")
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
    st.sidebar.header("customplot")
    st.sidebar.write("classify based on")
    g=st.sidebar.radio("what's your choice",('roll_no','cgpa','duesubjects'))
    if g=='roll_no':
        try:
            st.subheader("based on roll_no")
            k=df['roll_no'].unique().tolist()
            select=st.multiselect('select',k)
            k=df['roll_no'].isin(select)
            k=df[k].reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['cgpa'],k['credits']],
            )
            st.plotly_chart(g1)

        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets6.lottiefiles.com/datafiles/aba45c7b75d547282b2dbdc97969412b/progress_bar.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)

    elif g=='cgpa':
        st.subheader("based on cgpa")
        min=st.slider('select min cgpa',1,10,1)
        max=st.slider('select max cgpa',1,10,1)
        try:
            k=df[df['cgpa']>=min]
            k=k[k['cgpa']<=max]
            k=k.reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['cgpa'],k['credits']],
            )
            st.plotly_chart(g1)
        
        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets8.lottiefiles.com/private_files/lf30_cc9cxym5.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)
    
    elif g=='duesubjects':
        try:
            st.subheader("based on due_subjects")
            k=df['due_subjects'].unique().tolist()
            select=[' 0/8']
            select=st.sidebar.multiselect('select',k)
            k=df['due_subjects'].isin(select)
            k=df[k].reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['cgpa'],k['credits']],
            )
            st.plotly_chart(g1)

        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets8.lottiefiles.com/private_files/lf30_cc9cxym5.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)