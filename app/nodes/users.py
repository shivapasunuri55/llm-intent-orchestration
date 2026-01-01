from app.services.jsonplaceholder import get_users


def fetch_user(state):
    if not state.target_user_name:
        return {"approved": False, "stop_reason": "No target user specified"}
    users = get_users()
    target = state.target_user_name.strip().lower()
    for u in users:
        u_name = u.get("name", "").lower()
        # accept exact match or substring matches to be more forgiving of parsing
        if u_name == target or u_name in target or target in u_name:
            return {"user": u}
    return {"approved": False, "stop_reason": "User not found"} 
