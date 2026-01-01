from dotenv import load_dotenv

load_dotenv()
from app.graph.api_agent import agent

if __name__ == "__main__":
    tests = [
        # -------------------------
        # USER LOOKUP — single field
        # -------------------------
        "Is there a user with email Nathan@yesenia.net?",
        "Find users named Clementine Bauch",
        "Anyone with username Samantha?",
        "Check if there is a user called Ervin Howell",
        # -------------------------
        # USER LOOKUP — nested fields
        # -------------------------
        "Are there any users from McKenziehaven?",
        "Who works at Romaguera-Jacobson?",
        "Find users working at Romaguera-Jacobson in McKenziehaven",
        # -------------------------
        # USER LOOKUP — multiple filters
        # -------------------------
        "Find users named Clementine who work at Romaguera-Jacobson",
        "Is there a user named Clementine from McKenziehaven?",
        "Find users with username Samantha and email Nathan@yesenia.net",
        # -------------------------
        # POST QUERIES
        # -------------------------
        "How many posts are written by user 1?",
        "Are there any posts mentioning architecto?",
        "Find posts with the word suscipit in the body",
        "Count posts written by userId 3",
        # -------------------------
        # COMMENT QUERIES
        # -------------------------
        "Are there comments written by Eliseo@gardner.biz?",
        "Do any comments mention laudantium?",
        "Are there any comments for post 10?",
        "Check if comments exist on postId 5",
        # -------------------------
        # CROSS-ENTITY / JOIN-STYLE
        # -------------------------
        "Fetch comments on posts written by user 1",
        "Are there comments on posts by Clementine Bauch?",
        "Get comments for posts created by userId 2",
        # -------------------------
        # LANGUAGE / CONTENT FILTER
        # -------------------------
        "Are there any comments written in English?",
        "Check comments language for English text",
        # -------------------------
        # AMBIGUOUS / UNKNOWN
        # -------------------------
        "Tell me something interesting",
        "Analyze engagement",
        "Give insights",
        "Fetch data",
        "Hello",
    ]

    for q in tests:
        print("Q:", q)

        output = agent.invoke({"query": q})

        print("PLAN:")
        print(output.get("plan"))

        print("RESULT:")
        print(output.get("result"))
        print("DATA:")
        print(output.get("data"))

        print("-" * 50)
