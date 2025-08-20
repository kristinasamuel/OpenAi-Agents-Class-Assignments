# assignment_01/main.py
#  main file to run the agent with Chainlit
#  This file sets up the Chainlit interface and connects it with the agent

import  chainlit as cl
from agents import Runner
from my_agents.agents import Assisatnt_Agent
from my_config.config import model

# Chainlit event handlers
@cl.on_chat_start
async def start_chat():
    await cl.Message(content="Hello 👋 I'm your AI Assistant! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    # Get user input
    user_input = message.content

    # Run the agentwith user input
    response = Runner.run_sync(Assisatnt_Agent, user_input)

    # Send agent's reply back to user
    await cl.Message(content=f"AI Response: {response.final_output}").send()