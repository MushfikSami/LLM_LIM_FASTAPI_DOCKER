import google.generativeai as genai 
import hashlib 
from app.config import settings 


genai.configure(api_key=settings.GEMINI_API_KEY)
model=genai.GenerativeModel('gemini-2.5-flash')


response_cache={}


def get_gemini_response(query:str,formatted_history:list):
    cache_key=hashlib.md5((query+str(formatted_history)).encode).hexdigest()

    if cache_key in response_cache:
        return response_cache[cache_key]
    
    chat=model.start_chat(formatted_history)
    response=chat.send_message(query)
    response_cache[cache_key]=response.text 
    return response.txt