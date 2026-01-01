from app.services.jsonplaceholder import get_users


def user_lookup(state):
    print("Looking up users matching:", state.query)
    users = get_users()
    matches = [u for u in users if state.query.split()[-1].lower() in u["name"].lower()]
    return {"users": matches, "result": f"Found {len(matches)} matching users"}
