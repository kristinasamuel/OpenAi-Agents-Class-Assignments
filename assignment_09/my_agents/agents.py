# # agents.py

# hotel_assistant agent  
from agents import Agent
from my_connections.connect import model
from instructions.dynamic_instructions import dynamic_instruction

hotel_assistant = Agent(
    name="Hotel Customer Care",
    instructions=dynamic_instruction,
    model=model,
)
