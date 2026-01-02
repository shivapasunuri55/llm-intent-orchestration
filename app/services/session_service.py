import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Session


async def create_session(
    db: AsyncSession,
    *,
    user_id: uuid.UUID,
):
    new_session = Session(
        id=uuid.uuid4(),
        user_id=user_id,
    )
    db.add(new_session)
    try:
        await db.commit()
        await db.refresh(new_session)
    except Exception:
        await db.rollback()
        raise
    return new_session


async def get_session_by_id(
    db: AsyncSession,
    session_id: uuid.UUID,
) -> Session | None:
    return await db.get(Session, session_id)
