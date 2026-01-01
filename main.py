from app.graph.api_agent import agent

if __name__ == "__main__":
    query = input("Enter query: ")
    out = agent.invoke({"query": query})
    print("\nRESULT:", out.get("result"))
