from pydantic import BaseModel
from typing import Optional, List, Dict


class AgentState(BaseModel):
    query: str

    target_user_name: Optional[str] = None
    max_posts: Optional[int] = None

    user: Optional[Dict] = None
    posts: Optional[List[Dict]] = None
    comments: Optional[List[Dict]] = None

    approved: bool = True
    stop_reason: Optional[str] = None
