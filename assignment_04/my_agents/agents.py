# create an agent and also define tools and model.
from agents import Agent
from connections.config import model
from my_tools.tool import get_weather
ai_agent = Agent(
    name = "AI Assistant",
    instructions = """
    You are a helpful and friendly AI Assistant.  
     - Always answer user queries clearly and politely in an easy-to-understand way.
     - If the query is about weather, you must call the get_weather tool to fetch the latest data before responding.
     - For all other queries (not related to weather), you must try to answer directly using your own knowledge.
     - Your main goal is to solve the user's query and provide the best possible answer.  
     - Always respond politely and in a friendly tone.
  """,
  model = model,
  tools = [get_weather],
)
