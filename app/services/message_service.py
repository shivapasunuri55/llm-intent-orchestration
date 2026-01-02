import uuid
from typing import List, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models import Message


async def save_message(
    db: AsyncSession,
    *,
    session_id: uuid.UUID,
    role: str,
    content: str,
    plan: dict | None = None,
):
    message = Message(
        session_id=session_id,
        role=role,
        content=content,
        plan=plan,
    )
    db.add(message)
    await db.commit()


async def get_recent_messages(
    db: AsyncSession,
    *,
    session_id: uuid.UUID,
    limit: int = 10,
) -> List[Dict]:
    stmt = (
        select(Message)
        .where(Message.session_id == session_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
    )

    result = await db.execute(stmt)
    messages = result.scalars().all()

    return [{"role": m.role, "content": m.content} for m in reversed(messages)]
