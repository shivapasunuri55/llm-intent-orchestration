from app.graph.api_agent import api_agent

if __name__ == "__main__":
    query = input("Enter query: ")

    result = api_agent.invoke({"query": query})

    if result.get("stop_reason"):
        print("\n❌ STOPPED:", result["stop_reason"])
    else:
        print("\n✅ SUCCESS")
        print("Comments fetched:", len(result.get("comments", [])))
