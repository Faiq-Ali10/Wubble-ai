from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_agent

app = FastAPI()

class AgentRequest(BaseModel):
    prompt: str
    
class AgentResponse(BaseModel):
    response: str

@app.post("/agent", response_model=AgentResponse)
async def chat_agent(request: AgentRequest):
    result = run_agent(request.prompt)
    return {"response": result}
