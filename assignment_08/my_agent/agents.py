#  Agent
from agents import Agent
from my_connections.connect import model
from guardrials.guardrials import guardrial_input_function,guardrail_output_function

Math_Agent = Agent(
    name = "Professor Aman",
    instructions= "You are a helpful math agent. Your task is to handle user queries and solve math problems.",
    model = model,
    input_guardrails= [guardrial_input_function],
    output_guardrails= [guardrail_output_function]
)