from app.state.schema import AgentState
from app.llm.router import chain


def parse_query(state: AgentState):
    summary = ""
    history = ""

    for h in state.history or []:
        if h["role"] == "system" and h["content"].startswith("SESSION SUMMARY"):
            summary = h["content"]
        else:
            history += f"{h['role'].upper()}: {h['content']}\n"

    print("The payloads are:", state.query, summary, history)

    plan = chain.invoke(
        {
            "query": state.query,
            "summary": summary or "None",
            "history": history or "None",
        }
    )

    return {"plan": plan}
