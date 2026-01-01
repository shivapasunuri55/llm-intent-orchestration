from app.services.jsonplaceholder import get_comments_by_post


def fetch_comments(state):
    all_comments = []
    for post in state.posts:
        all_comments.extend(get_comments_by_post(post["id"]))
    return {"comments": all_comments}
