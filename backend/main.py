from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()          #create app

#Test route
@app.get("/")            #define route
def home():
    return {"message": "Backend is working"}

#Request body structure
class ChatRequest(BaseModel):
    query: str       #tells backend-User will send JSON with a query str

#Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    return{
        "response": f"You asked: {request.query}"
    }