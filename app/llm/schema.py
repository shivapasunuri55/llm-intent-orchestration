from pydantic import BaseModel
from typing import List, Optional, Literal


class Filter(BaseModel):
    field: str
    value: str


class QueryPlan(BaseModel):
    intent: Literal["LOOKUP", "COUNT", "EXISTS", "FILTER", "UNKNOWN"]
    entity: Optional[Literal["user", "post", "comment"]] = None
    filters: Optional[List[Filter]] = None
