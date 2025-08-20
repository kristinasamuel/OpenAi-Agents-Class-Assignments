#  assignment_01/my_agents/agents.py
#  assistant agent

from agents import Agent
from my_config.config import model

Assisatnt_Agent = Agent(
    name = "Assistant Agent",
    instructions= """
        - You are a knowledgeable and friendly AI assistant.
        - Your role is to clearly understand the user's questions and provide accurate answers.  
     """,
    model = model,
)
