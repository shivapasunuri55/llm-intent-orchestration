from app.services.jsonplaceholder import get_users, get_posts_by_user


def post_count(state):
    users = get_users()
    user = users[0]  # simplified lookup
    posts = get_posts_by_user(user["id"])
    return {"result": f"{user['name']} has {len(posts)} posts"}
