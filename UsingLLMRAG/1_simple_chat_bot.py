from utils import get_chat_model
import streamlit as st

llm = get_chat_model()
st.set_page_config(
    page_title="Simple Chat Bot",
    page_icon="https://freesvg.org/img/1538298822.png",   
    layout="centered"                  
)

st.title("Simple Chat Bot")
st.write("Hii There")

query = st.text_input("Enter Your Query :")

if st.button("Process"):
    
    responce = llm.invoke(query)
    st.write(responce.content)