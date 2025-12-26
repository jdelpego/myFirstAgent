from langchain.tools import tool
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    count: int

@tool
def add1(state: State) -> State:
    """Adds 1 to the current count in state"""
    return {"count": state["count"] + 1}
    


builder = StateGraph(State)
builder.add_node(add1)
builder.add_edge(START, add1)
builder.add_edge(add1, END)
agent = builder.compile()
response = agent.invoke({"count": 0})
print(response)
