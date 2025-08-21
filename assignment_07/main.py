# Run Agent 
from agents import Runner
from my_agents.agent import general_agent
def main():
    msg = input("Please Enter your query : ")
    result = Runner.run_sync(general_agent, msg)
    print(f"\nAgent Response:\n{result.final_output}")

if __name__ == "__main__":
    main()



#  Enter your query : what is the weather of karachi

# Agent Response:
# The weather in Karachi is currently 28.1°C with moderate or heavy rain and thunder. The wind is blowing from the south at 5.0 kph. The humidity is 89%.      