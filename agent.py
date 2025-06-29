from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat


import os
from dotenv import load_dotenv
load_dotenv()
os.environ["groq_api_key"]=os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=Groq(id="llama3-70b-8192"),
    description="you are a helpful assistant please answer the question",
    tools=[DuckDuckGoTools()],
    markdown=True,
    show_tool_calls=True
)
agent.print_response("what is the latest news in india")