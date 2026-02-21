from fastapi import Header, HTTPException 
from config import settings 


async def  verify_api_key(x_api_key:str=Header(...)):
    if x_api_key!=settings.API_KEY_KEY:
        raise HTTPException(status_code=401,detail='Unauthorized')
    return x_api_key