import streamlit as st 
import os 
import requests 

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8080")

st.set_page_config(page_title='GEMINI BOT WITH HISTORY')
st.header('GEMINI BOT')


if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


if 'gemini_history' not in st.session_state:
    st.session_state['gemini_history']=[]

input=st.text_input('INPUT: ',key='input') 
submit=st.button("ASK") 


if input and submit:
    payload={
        'query':input,
        'history':st.session_state['gemini_history']
    }

    try:
        response=requests.post(f'{BACKEND_URL}/chat',json=payload)
        response.raise_for_status()
        bot_reply=response.json().get('reply')
        st.session_state['chat_history'].append(('YOU',input))
        st.session_state['chat_history'].append(("BOT",bot_reply))


        st.session_state['gemini_history'].append({'role':'user','parts':input})
        st.session_state['gemini_history'].append({'role':'model','parts':bot_reply})


    except requests.exceptions.RequestException as e:
        st.error(f'Error connecting to backend: {e}') 

st.subheader("History: ")
for role,message in st.session_state['chat_history']:
    st.write(f'{role} : {message}')
