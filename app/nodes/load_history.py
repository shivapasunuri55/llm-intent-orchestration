import uuid
from app.state.schema import AgentState
from app.services.message_service import get_recent_messages


async def load_history(state: AgentState, *, config) -> dict:
    db = config["configurable"]["db"]
    print("Loading history for session:", state.session_id)

    history = await get_recent_messages(
        db,
        session_id=uuid.UUID(state.session_id),
        limit=10,
    )

    print(f"Loaded {len(history)} messages from history.")

    return {"history": history}
