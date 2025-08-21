# create an agent in this we call multiple tool for better response

from agents import Agent
from my_connections.connect import model
from my_tools.tools import Math_Tool, Weather_Tool, get_latest_news

Assistant_Agent = Agent(
    name="AI Assistant",
    instructions = """
    You are a helpful and friendly AI Assistant.
    - Answer all user queries clearly and respectfully.  
    - For math-related questions, use Math_Tool.  
    - For weather-related questions, use Weather_Tool.  
    - For news-related questions, use get_latest_news.  
    - Always respond politely and in a friendly tone.
    """,
    model=model,
    tools = [Math_Tool, Weather_Tool, get_latest_news]
)
