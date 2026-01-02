import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app import db
from app.graph.api_agent import agent
from app.db.session import get_db

from app.services.user_service import create_user
from app.services.session_service import create_session

router = APIRouter()

router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    session_id: str | None = None
    user_id: str | None = "anonymous"


class ChatResponse(BaseModel):
    session_id: str
    plan: dict | None
    result: str | None
    data: list | None


class CreateUserResponse(BaseModel):
    id: str


class CreateSessionRequest(BaseModel):
    user_id: str | None = None


class CreateSessionResponse(BaseModel):
    session_id: str
    user_id: str


class ErrorResponse(BaseModel):
    detail: str


@router.post(
    "/create_user",
    response_model=CreateUserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_request(db: AsyncSession = Depends(get_db)):
    try:
        user = await create_user(db=db, id=uuid.uuid4())
        return CreateUserResponse(id=str(user.id))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create user: {e}",
        )


@router.post(
    "/create_session",
    response_model=CreateSessionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_session_request(
    req: CreateSessionRequest,
    db: AsyncSession = Depends(get_db),
):
    try:
        user_id = uuid.UUID(req.user_id) if req.user_id else uuid.uuid4()
        session = await create_session(db=db, user_id=user_id)

        return CreateSessionResponse(
            session_id=str(session.id),
            user_id=str(session.user_id),
        )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID format for user_id",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create session: {e}",
        )


@router.post("/chat", response_model=ChatResponse)
async def chat(
    req: ChatRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Executes the intent-orchestrated workflow
    with session-based memory persistence.
    """

    # 1️⃣ Resolve or create session id
    session_id = uuid.UUID(req.session_id) if req.session_id else uuid.uuid4()

    # 2️⃣ Invoke graph (async + DB injected)
    output = await agent.ainvoke(
        {
            "query": req.query,
            "session_id": str(session_id),
            "user_id": req.user_id,
        },
        config={"configurable": {"db": db}},
    )

    # 3️⃣ Return response (unchanged semantics)
    return {
        "session_id": str(session_id),
        "plan": output.get("plan").model_dump() if output.get("plan") else None,
        "result": output.get("result"),
        "data": output.get("data"),
    }
