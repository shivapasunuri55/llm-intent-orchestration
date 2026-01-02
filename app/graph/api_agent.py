from langgraph.graph import StateGraph, END
from app.state.schema import AgentState
from app.nodes.intent import parse_query
from app.nodes.approval import human_approval
from app.nodes.users import user_lookup
from app.nodes.posts import post_lookup
from app.nodes.comments import comment_lookup
from app.nodes.load_history import load_history
from app.nodes.persist_interaction import persist_interaction
from app.nodes.summarize_history import summarize_history

graph = StateGraph(AgentState)

graph.add_node("load_history", load_history)
graph.add_node("parse_query", parse_query)
graph.add_node("persist_interaction", persist_interaction)
graph.add_node("summarize_history", summarize_history)

graph.add_node("approve_user", lambda s: human_approval(s, "User Lookup"))
graph.add_node("approve_post", lambda s: human_approval(s, "Post Lookup"))
graph.add_node("approve_comment", lambda s: human_approval(s, "Comment Lookup"))

graph.add_node("user_lookup", user_lookup)
graph.add_node("post_lookup", post_lookup)
graph.add_node("comment_lookup", comment_lookup)

graph.set_entry_point("load_history")
graph.add_edge("load_history", "summarize_history")
graph.add_edge("summarize_history", "parse_query")


def route_by_plan(state: AgentState):
    """
    Route execution based on the entity extracted
    by the LLM query planner.
    """
    if not state.plan:
        return END

    if state.plan.intent == "UNKNOWN":
        return END

    return state.plan.entity


graph.add_conditional_edges(
    "parse_query",
    route_by_plan,
    {
        "user": "approve_user",
        "post": "approve_post",
        "comment": "approve_comment",
        "__end__": "persist_interaction",
    },
)

graph.add_edge("approve_user", "user_lookup")
graph.add_edge("approve_post", "post_lookup")
graph.add_edge("approve_comment", "comment_lookup")

graph.add_edge("user_lookup", "persist_interaction")
graph.add_edge("post_lookup", "persist_interaction")
graph.add_edge("comment_lookup", "persist_interaction")

graph.add_edge("persist_interaction", END)

agent = graph.compile()
