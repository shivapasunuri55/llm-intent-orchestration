from app.state.schema import AgentState
from app.llm.router import chain


def _format_history(history: list) -> str:
    if not history:
        return "None"

    return "\n".join(f"{h['role'].upper()}: {h['content']}" for h in history)


def parse_query(state: AgentState):
    plan = chain.invoke(
        {
            "query": state.query,
            "history": _format_history(state.history),
        }
    )

    return {"plan": plan}
