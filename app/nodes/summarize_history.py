import uuid
from app.state.schema import AgentState
from app.services.session_service import get_session_by_id, update_session_summary
from app.llm.summarizer import summarize_chain


MAX_RECENT_MESSAGES = 6


def _format_for_summary(history: list) -> str:
    return "\n".join(f"{h['role'].upper()}: {h['content']}" for h in history)


async def summarize_history(state: AgentState, *, config) -> dict:
    db = config["configurable"]["db"]
    session_id = uuid.UUID(state.session_id)

    if len(state.history) <= MAX_RECENT_MESSAGES:
        return {}

    session = await get_session_by_id(db, session_id)

    old_history = state.history[:-MAX_RECENT_MESSAGES]
    recent_history = state.history[-MAX_RECENT_MESSAGES:]

    updated_summary = summarize_chain.invoke(
        {
            "existing_summary": session.summary or "None",
            "history": _format_for_summary(old_history),
        }
    )

    await update_session_summary(
        db,
        session_id=session_id,
        summary=updated_summary.content,
    )

    # Replace history with summary + recent messages
    return {
        "history": [
            {
                "role": "system",
                "content": f"SESSION SUMMARY: {updated_summary.content}",
            }
        ]
        + recent_history
    }
