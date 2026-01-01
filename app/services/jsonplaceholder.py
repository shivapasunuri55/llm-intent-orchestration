import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(f"{BASE_URL}/users").json()


def get_posts_by_user(user_id: int):
    return requests.get(f"{BASE_URL}/posts", params={"userId": user_id}).json()


def get_comments_by_post(post_id: int):
    return requests.get(f"{BASE_URL}/comments", params={"postId": post_id}).json()
