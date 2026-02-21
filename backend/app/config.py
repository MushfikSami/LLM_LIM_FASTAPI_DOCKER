from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    GEMINI_API_KEY:str 
    API_KEY_KEY:str='api_key'

    class Config:
        env_file='.env'



settings=Settings()        
