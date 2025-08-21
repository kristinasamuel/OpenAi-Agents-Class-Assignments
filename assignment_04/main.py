# main file to run the agent
from agents import Runner
from my_agents.agents import ai_agent
import asyncio

# function to execute the runner
def main():
    print("Hello how can I assist you today!")
    user_input = input("Enter your query: ")
    response =  Runner.run_sync(ai_agent, user_input)
    print(f"Agent Response: {response.final_output}")
main()


# final output
# Hello how can I assist you today!
# Enter your query: what is the weather of lahore
# <<<<<< Weather Tool Call >>>>>.
# Agent Response: The weather in Lahore is 35.2°C and partly cloudy.