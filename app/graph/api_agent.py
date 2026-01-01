from langgraph.graph import StateGraph, END
from app.state.schema import AgentState

from app.nodes.intent import parse_intent
from app.nodes.users import fetch_user
from app.nodes.posts import fetch_posts
from app.nodes.comments import fetch_comments
from app.nodes.approval import human_approval

graph = StateGraph(AgentState)

# core nodes
graph.add_node("intent", parse_intent)
graph.add_node("user", fetch_user)
graph.add_node("posts", fetch_posts)
graph.add_node("comments", fetch_comments)

# approval wrappers
graph.add_node("approve_intent", lambda s: human_approval(s, "Parse Intent"))
graph.add_node("approve_user", lambda s: human_approval(s, "Fetch User"))
graph.add_node("approve_posts", lambda s: human_approval(s, "Fetch Posts"))
graph.add_node("approve_comments", lambda s: human_approval(s, "Fetch Comments"))

graph.set_entry_point("intent")

graph.add_edge("intent", "approve_intent")
graph.add_edge("approve_intent", "user")
graph.add_edge("user", "approve_user")
graph.add_edge("approve_user", "posts")
graph.add_edge("posts", "approve_posts")
graph.add_edge("approve_posts", "comments")
graph.add_edge("comments", "approve_comments")
graph.add_edge("approve_comments", END)

api_agent = graph.compile()
