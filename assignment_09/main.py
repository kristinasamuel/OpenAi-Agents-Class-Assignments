# main.py
from agents import Runner
from my_agents.agents import hotel_assistant

print("👋 Hi! I am your Hotel Assistant. How may I help you today?")
user_input = input("Enter your query: ") 
context = {"user_query": user_input}
res = Runner.run_sync(starting_agent=hotel_assistant,input=user_input,context=context)
print(res.final_output)


# 👋 Hi! I am your Hotel Assistant. How may I help you today?
# Enter your query: How many rooms are available in Hotel Pearl?
# There are 140 rooms available in Hotel Pearl.
