from app.services.jsonplaceholder import get_posts_by_user
from app.utils.field_validation import validate_filters


def post_lookup(state):
    plan = state.plan

    if not validate_filters("post", plan.filters):
        return {"result": "Invalid filter field for post entity."}

    posts = []
    for f in plan.filters or []:
        if f.field == "userId":
            posts = get_posts_by_user(int(f.value))

    return {"data": posts, "result": f"Found {len(posts)} posts"}
