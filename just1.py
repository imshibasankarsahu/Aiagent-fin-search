# app.py
import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["groq_api_key"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # Optional

# Build agents
web_agent = Agent(
    name="web_agent",
    role="Search the web",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGoTools()],
    instructions="Always include source",
    show_tool_calls=True,
    markdown=True
)

fin_agent = Agent(
    name="finance_agent",
    role="Get financial information",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
    )],
    instructions="Use table to show data",
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[fin_agent, web_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include source", "Use table to show data"],
    show_tool_calls=True,
    markdown=True
)

# Streamlit UI
st.title("📊 AI Agent for Finance + News")

query = st.text_input("Ask something (e.g., 'News about Tesla', 'Stock price of Apple')")

if query:
    with st.spinner("Working..."):
        result = agent_team.run(message=query)
        st.markdown(result.content)
