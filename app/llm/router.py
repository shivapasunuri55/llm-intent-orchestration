from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from app.llm.schema import QueryPlan

parser = PydanticOutputParser(pydantic_object=QueryPlan)

PROMPT = PromptTemplate(
    template="""
        You are a query planning system.

        Supported entities and fields:

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

        Rules:
        - Choose exactly ONE intent.
        - Choose exactly ONE entity.
        - Extract ALL relevant filters.
        - Use only allowed fields.
        - Use exact values from the query.
        - If unsure, return intent UNKNOWN.
        - Output valid JSON only.

        User query:
        {query}

        {format_instructions}
""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

chain = PROMPT | llm | parser
