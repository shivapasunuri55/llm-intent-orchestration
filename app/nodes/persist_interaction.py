import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app import db
from app.state.schema import AgentState
from app.services.message_service import save_message


async def persist_interaction(
    state: AgentState,
    *,
    config,
) -> dict:
    """
    Persist the user query and system response
    for the current session.
    """
    db = config["configurable"]["db"]
    session_id = uuid.UUID(state.session_id)

    # Save user message
    await save_message(
        db,
        session_id=session_id,
        role="user",
        content=state.query,
    )

    # Save system response
    await save_message(
        db,
        session_id=session_id,
        role="system",
        content=state.result or "",
        plan=state.plan.model_dump() if state.plan else None,
    )

    # No state changes required
    return {}
