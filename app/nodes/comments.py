from app.services.jsonplaceholder import get_comments_by_post
from app.utils.field_validation import validate_filters


def comment_lookup(state):
    plan = state.plan

    if not validate_filters("comment", plan.filters):
        return {"result": "Invalid filter field for comment entity."}

    comments = []
    for f in plan.filters or []:
        if f.field == "postId":
            comments.extend(get_comments_by_post(int(f.value)))

    return {"data": comments, "result": f"Found {len(comments)} comments"}
