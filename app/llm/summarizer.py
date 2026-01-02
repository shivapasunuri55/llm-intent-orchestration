from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

SUMMARY_PROMPT = PromptTemplate(
    template="""
        You are summarizing a conversation for long-term memory.

        Rules:
        - Be concise
        - Preserve factual information
        - Preserve user intent and constraints
        - Do NOT include greetings or filler
        - Do NOT invent information

        Existing summary:
        {existing_summary}

        New conversation chunk:
        {history}

        Return an updated summary.
""",
    input_variables=["existing_summary", "history"],
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

summarize_chain = SUMMARY_PROMPT | llm
