from agents import Runner
from my_agents.agents import Math_Agent

def main():

    print("\nMath Agent: How can i assist you: \n")
    #  user prompt 
    prompt = input("Enter your prompt: ")
    #  run agents 
    response = Runner.run_sync(Math_Agent,prompt)
    print("Agent Response:",response.final_output)


if __name__ == "__main__":
    main()

# output:

# Math Agent: How can i assist you: 
# Enter your prompt: 43 + 78
# >>>>>> Addition function called >>>>>>>>
# Agent Response: The sum of 43 and 78 is 121.

# Math Agent: How can i assist you:
# Enter your prompt: 43 - 23
# >>>>>> Subtractions function called >>>>>>>>
# Agent Response: The result of 43 - 23 is 20.

# Math Agent: How can i assist you: 
# Enter your prompt: 3 / 3
# >>>>>> Divisions function called >>>>>>>>
# Agent Response: The result of the division 3 / 3 is 1.0.


