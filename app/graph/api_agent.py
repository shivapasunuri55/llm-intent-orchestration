from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import StateGraph, END
from app.state.schema import AgentState

from app.nodes.intent import parse_intent
from app.nodes.approval import human_approval
from app.nodes.users import user_lookup
from app.nodes.posts import post_count
from app.nodes.comments import comment_existence

graph = StateGraph(AgentState)

graph.add_node("intent", parse_intent)

graph.add_node("approve_users", lambda s: human_approval(s, "Users API"))
graph.add_node("approve_posts", lambda s: human_approval(s, "Posts API"))
graph.add_node("approve_comments", lambda s: human_approval(s, "Comments API"))

graph.add_node("users", user_lookup)
graph.add_node("posts", post_count)
graph.add_node("comments", comment_existence)

graph.set_entry_point("intent")


def route_intent(state):
    return state.intent


graph.add_conditional_edges(
    "intent",
    route_intent,
    {
        "USER_LOOKUP": "approve_users",
        "POST_COUNT": "approve_posts",
        "COMMENT_EXISTENCE": "approve_comments",
        "UNKNOWN": END,
    },
)

graph.add_edge("approve_users", "users")
graph.add_edge("approve_posts", "posts")
graph.add_edge("approve_comments", "comments")

graph.add_edge("users", END)
graph.add_edge("posts", END)
graph.add_edge("comments", END)

agent = graph.compile()
