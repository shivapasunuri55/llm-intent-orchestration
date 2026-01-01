import re
from app.state.schema import AgentState


def parse_intent(state: AgentState):
    # deterministic extraction (on purpose)
    # capture the user name but stop at common delimiters like 'on', 'for', 'with', or end of string
    name_match = re.search(r"user\s+([A-Za-z\s]+?)(?:\s+on\b|\s+for\b|\s+with\b|$)", state.query, re.IGNORECASE)
    post_match = re.search(r"(\d+)\s+posts", state.query, re.IGNORECASE)

    return {
        "target_user_name": name_match.group(1).strip() if name_match else None,
        "max_posts": int(post_match.group(1)) if post_match else 10,
    }
