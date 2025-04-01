from langgraph.graph import StateGraph
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from typing import TypedDict
import os

# Load the API key from environment variables (via .env)
groq_api_key = os.getenv('GROQ_API_KEY')

# Define the AgentState
class AgentState(TypedDict):
    query: str
    response: str
    
    