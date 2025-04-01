from langgraph.graph import StateGraph
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from typing import TypedDict
import os
from dotenv import load_dotenv

load_dotenv()

# Load the API key from environment variables (via .env)
groq_api_key = os.getenv('GROQ_API_KEY')

# Define the AgentState
class AgentState(TypedDict):
    query: str
    response: str
    
# Initialize the ChatGroq model
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, groq_api_key=groq_api_key)

# Define the agent function that processes the query
def agent(state: AgentState) -> AgentState:
    query = state["query"]
    response = llm([HumanMessage(content=query)])
    return {"response": response.content}

# Set up LangGraph workflow
def create_workflow():
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", agent)
    workflow.set_entry_point("agent")
    workflow.set_finish_point("agent")
    return workflow

# Compile and run the workflow
def run_agent_workflow(query: str):
    workflow = create_workflow()
    graph = workflow.compile()
    result = graph.invoke({"query": query})
    return result["response"]