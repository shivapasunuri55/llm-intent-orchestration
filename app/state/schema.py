from pydantic import BaseModel
from typing import Optional, List, Dict, Literal


class AgentState(BaseModel):
    query: str

    intent: Optional[
        Literal[
            "USER_LOOKUP",
            "POST_COUNT",
            "COMMENT_EXISTENCE",
            "COMMENT_LANGUAGE",
            "UNKNOWN",
        ]
    ] = None

    users: Optional[List[Dict]] = None
    posts: Optional[List[Dict]] = None
    comments: Optional[List[Dict]] = None

    result: Optional[str] = None
    approved: bool = True
