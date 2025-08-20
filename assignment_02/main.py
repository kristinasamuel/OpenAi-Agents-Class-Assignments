from agents import Runner
from my_connections.config import model
from my_agents.agents import agent

def main():
    # user prompt
    prompt = input ("Enter your question:")
    # run the agent
    result = Runner.run_sync(agent,prompt)
    print(f"Agent Response: {result.final_output}")

if __name__ == "__main__":
    main()