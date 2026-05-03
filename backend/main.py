from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
app = FastAPI()          #create app

#Test route
@app.get("/")            #define route
def home():
    return {"message": "Backend is working"}

#Request body structure
class ChatRequest(BaseModel):
    query: str       #tells backend-User will send JSON with a query str
    api_key: str

#Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        # Configure Gemini with user's API key (BYOK)
        genai.configure(api_key=request.api_key)

        #Load model
        model=genai.GenerativeModel("models/gemini-1.5-flash")

        #Generate response
        response=model.generate_content(request.query)

        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}