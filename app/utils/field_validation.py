ALLOWED_FIELDS = {
    "user": {
        "id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "company.name",
        "address.city",
    },
    "post": {"id", "userId", "title", "body"},
    "comment": {"id", "postId", "name", "email", "body"},
}


def validate_filters(entity: str, filters: list):
    if not filters:
        return True

    allowed = ALLOWED_FIELDS.get(entity, set())
    return all(f.field in allowed for f in filters)
