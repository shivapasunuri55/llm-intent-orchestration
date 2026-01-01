from app.state.schema import AgentState
from app.llm.router import chain


def parse_intent(state: AgentState):
    out = chain.invoke({"query": state.query})
    return {"intent": out.intent}
