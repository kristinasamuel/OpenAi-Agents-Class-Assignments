# main file to execute the Assistant Agent

from agents import Runner
from my_agent.assistant_agent import Assistant_Agent

def main():
    print("Hi,I am Assistant Agent.How can i help you.\n")
    user_prompt = input("Please enter your query: ")
    result = Runner.run_sync(Assistant_Agent, user_prompt)
    print("Assistant Agent Response:", result.final_output)

main()

# Final output

# Hi,I am Assistant Agent.How can i help you.
# Please enter your query: what is weather in karachi
# >>>>>> Weather Tool Activated >>>>>>
# Assistant Agent Response: The weather in Karachi is cloudy with a temperature of 27°C.

# Hi,I am Assistant Agent.How can i help you.
# Please enter your query: add 3 + 5   
# >>>>> Math Tool Activated.>>>>>
# Assistant Agent Response: Okay! So, the answer of 3 + 5 is 8.

# Hi,I am Assistant Agent.How can i help you.
# Please enter your query: what is the today news 
# >>>>> News Tool Activated.>>>>>
# Assistant Agent Response: Today's news: OpenAI releases new AI model that can understand and generate human-like text.

