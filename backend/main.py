from fastapi import FastAPI,HTTPException 
import google.generativeai as genai 
import os 
from dotenv import load_dotenv 
from pydantic import BaseModel 
from typing import List, Dict,Any

app=FastAPI(title='Gemini Bot API')

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model=genai.GenerativeModel('gemini-2.5-flash')

class ChatRequest(BaseModel):
    query:str 
    history:List[Dict[str,Any]]=[]



@app.post('/chat')
async def chat_endpoint(request:ChatRequest):
    try:
        formatted_history=[
            {'role':msg['role'],'parts':[msg['parts']]}
            for msg in request.history
        ]    

        chat=model.start_chat(history=formatted_history)
        response=chat.send_message(request.query)
        return {'reply':response.text}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    