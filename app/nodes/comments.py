from app.services.jsonplaceholder import (
    get_users,
    get_posts_by_user,
    get_comments_by_post,
)


def comment_existence(state):
    users = get_users()
    user = users[0]
    posts = get_posts_by_user(user["id"])

    comments = []
    for p in posts:
        comments.extend(get_comments_by_post(p["id"]))

    return {"result": f"Found {len(comments)} comments"}
