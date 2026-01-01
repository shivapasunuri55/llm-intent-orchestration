from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.api_agent import agent

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    plan: dict | None
    result: str | None
    data: list | None


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    Executes the intent-orchestrated workflow
    and returns structured results.
    """
    output = agent.invoke({"query": req.query})

    return {
        "plan": output.get("plan").model_dump() if output.get("plan") else None,
        "result": output.get("result"),
        "data": output.get("data"),
    }
