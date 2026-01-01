from app.services.jsonplaceholder import get_posts_by_user


def fetch_posts(state):
    if not getattr(state, "user", None):
        return {"approved": False, "stop_reason": "No user available to fetch posts for"}
    posts = get_posts_by_user(state.user["id"])
    return {"posts": posts[: state.max_posts]}
