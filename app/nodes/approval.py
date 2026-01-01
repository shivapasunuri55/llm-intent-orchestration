from app.state.schema import AgentState


def human_approval(state: AgentState, step_name: str):
    print(f"\n🔍 APPROVAL REQUIRED: {step_name}")
    print("Current state snapshot:")
    print(state.model_dump(exclude_none=True))

    choice = input("Approve? (y/n): ").strip().lower()

    if choice != "y":
        return {"approved": False, "stop_reason": f"Human rejected step: {step_name}"}

    return {"approved": True}
