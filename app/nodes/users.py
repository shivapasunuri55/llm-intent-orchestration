from app.services.jsonplaceholder import get_users
from app.utils.field_validation import validate_filters


def user_lookup(state):
    plan = state.plan

    if plan.intent == "UNKNOWN":
        return {"result": "Cannot understand the query."}

    if not validate_filters("user", plan.filters):
        return {"result": "Invalid filter field for user entity."}

    users = get_users()

    def match(user, flt):
        value = flt.value.lower()

        if flt.field == "company.name":
            return value in user["company"]["name"].lower()
        if flt.field == "address.city":
            return value in user["address"]["city"].lower()

        return value in str(user.get(flt.field, "")).lower()

    results = users
    for f in plan.filters or []:
        results = [u for u in results if match(u, f)]

    return {"data": results, "result": f"Found {len(results)} matching users"}
