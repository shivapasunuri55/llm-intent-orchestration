from app.state.schema import AgentState
from app.llm.router import chain


def parse_query(state: AgentState):
    plan = chain.invoke({"query": state.query})
    return {"plan": plan}
