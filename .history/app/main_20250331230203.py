from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the request schema
class QueryRequest(BaseModel):
    query: str

@app.post("/generate/")
async def generate_response(request: QueryRequest):
    try:
        result = run_agent_workflow(request.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Agentic AI FastAPI application!"}
