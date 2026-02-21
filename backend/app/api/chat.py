from fastapi import APIRouter, Depends,HTTPException 
from pydantic import BaseModel 
from typing import List,Dict,Any 
from app.dependencies import verify_api_key 
from app.services.gemini_ml import get_gemini_response 

router=APIRouter(dependencies=[Depends(verify_api_key)])

class ChatRequest(BaseModel):
    query:str 
    history:List[Dict[str,Any]]=[]


@router.post('/chat')
async def chat_endpoint(request:ChatRequest):
    try:
        formatted_history=[
            {'role':msg['role'],'parts':[msg['parts']]}
            for msg in request.history
        ]

        reply=get_gemini_response(request.query,formatted_history)
        return {'reply':reply}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))