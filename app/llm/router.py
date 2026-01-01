from dotenv import load_dotenv

load_dotenv()
from pydantic import BaseModel
from typing import Literal
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI


class IntentOutput(BaseModel):
    intent: Literal[
        "USER_LOOKUP", "POST_COUNT", "COMMENT_EXISTENCE", "COMMENT_LANGUAGE", "UNKNOWN"
    ]


parser = PydanticOutputParser(pydantic_object=IntentOutput)

PROMPT = PromptTemplate(
    template="""
        You are an intent classification system.

        Classify the user query into ONE intent:

        - USER_LOOKUP → find users by name
        - POST_COUNT → count posts by a user
        - COMMENT_EXISTENCE → check if comments exist
        - COMMENT_LANGUAGE → check comment language
        - UNKNOWN → none apply

        User query:
        {query}

        {format_instructions}
""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

chain = PROMPT | llm | parser
