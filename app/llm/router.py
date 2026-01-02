from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from app.llm.schema import QueryPlan

parser = PydanticOutputParser(pydantic_object=QueryPlan)

PROMPT = PromptTemplate(
    template="""
        You are a query planning system for an API-backed application.

        You are given:
        1. A SESSION SUMMARY (long-term memory)
        2. RECENT CONVERSATION HISTORY
        3. The CURRENT USER QUERY

        Use the summary and history only for context.
        The CURRENT QUERY determines the action.

        ----------------------------------------
        SESSION SUMMARY:
        {summary}

        ----------------------------------------
        RECENT HISTORY:
        {history}

        ----------------------------------------
        SUPPORTED ENTITIES AND FIELDS:

        USER:
        - id
        - name
        - username
        - email
        - phone
        - website
        - company.name
        - address.city

        POST:
        - id
        - userId
        - title
        - body

        COMMENT:
        - id
        - postId
        - name
        - email
        - body

        ----------------------------------------
        RULES:
        - Choose exactly ONE intent.
        - Choose exactly ONE entity.
        - Extract ALL relevant filters.
        - Use ONLY allowed fields.
        - Use EXACT values from the query or context.
        - Use conversation context to resolve references
        (e.g., "that user", "their posts").
        - If the request is unclear or missing required information,
        return intent UNKNOWN.
        - Output VALID JSON ONLY.

        ----------------------------------------
        CURRENT USER QUERY:
        {query}

        {format_instructions}
""",
    input_variables=["query", "summary", "history"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

chain = PROMPT | llm | parser
