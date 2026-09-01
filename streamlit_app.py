import streamlit as st 
from openai import OpenAI

st.set_page_config(page_title= "Lab assignments HCAI", page_icon=None, layout="wide",
initial_sidebar_state="auto")

page1 = st.Page('Lab1.py', title = "Lab 1")
page2 = st.Page('Lab2.py', title = "Lab 2")

pg = st.navigation([page1, page2])
st.set_page_config(page_title= "Multipage Application - IST688 HCAI")
pg.run()