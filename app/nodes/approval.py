from app.state.schema import AgentState


def human_approval(state: AgentState, step: str):
    print(f"\n🔍 APPROVAL REQUIRED → {step}")
    print("Current state:", state.model_dump(exclude_none=True))

    if input("Approve? (y/n): ").strip().lower() != "y":
        return {"approved": False, "result": f"Stopped by human at step: {step}"}

    return {"approved": True}
