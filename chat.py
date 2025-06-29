from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools


import os
from dotenv import load_dotenv
load_dotenv()
os.environ["groq_api_key"]=os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

web_agent=Agent(
    name="web_agent",
    role="search on the web",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGoTools()],
    instructions="Always include source",
    show_tool_calls=True,
    markdown=True
)

fin_agent=Agent(
    name="finance agent",
    role="get finance information",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    instructions="use table to show data",
    show_tool_calls=True,
    markdown=True

)

agent_team=Agent(
    team=[fin_agent,web_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["always include source ","use table to show data"],
    show_tool_calls=True,
    markdown=True

)

agent_team.print_response("any news about tesla")