from pydantic import BaseModel
from typing import Optional, List, Dict
from app.llm.schema import QueryPlan


class AgentState(BaseModel):
    query: str
    session_id: str
    plan: Optional[QueryPlan] = None
    history: List[Dict] = []
    users: Optional[List[Dict]] = None
    posts: Optional[List[Dict]] = None
    comments: Optional[List[Dict]] = None
    data: Optional[List[Dict]] = None
    result: Optional[str] = None
    approved: bool = True
