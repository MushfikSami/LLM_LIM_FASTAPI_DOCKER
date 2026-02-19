from dotenv import load_dotenv 
import streamlit as st 
import google.generativeai as genai 
import os

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_gemini_answer(question):
    model=genai.GenerativeModel('gemini-2.5-flash-lite')
    response=model.generate_content(question)
    return response.text 

st.set_page_config(page_title='GEMINI AI WITH FASTAPI')
st.header("GEMINI BOT")
input=st.text_input("Input: ",key='Input') 

submit=st.button('Ask the question')

if submit:
    response=get_gemini_answer(input)
    st.subheader("ANSWER: ")
    st.write(response)