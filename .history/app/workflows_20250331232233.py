from .agent import run_agent_workflow

# You can keep the workflow-related logic in this file for modularity
def execute_workflow(query: str):
    return run_agent_workflow(query)
