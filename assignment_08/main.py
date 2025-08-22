# Main file to execute the agent
from agents import Runner
from  my_agent.agents import Math_Agent
def main():
    try:
        prompt = input("Enter your questions: ")
        result = Runner.run_sync(Math_Agent,prompt)
        print(result.final_output)
    except Exception as ex:
        print("Tripwire triggered! Guardrial activated.",ex)     

main()