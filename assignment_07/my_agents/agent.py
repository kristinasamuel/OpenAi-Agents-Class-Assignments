from agents import Agent
from my_config.config import model
from my_tools.tool import tavily_web_search

# create an agent 
general_agent = Agent(
    name="General Assistant",
    instructions="You are a smart and polite assistant. Use Tavily search if user asks about web information.",
    model=model,
    tools=[tavily_web_search], 
)