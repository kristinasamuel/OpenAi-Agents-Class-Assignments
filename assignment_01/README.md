# OpenAISDK Class Assignments

## Assignment 01: Build a Simple Agent

### Task
- Build a simple agent using **Python** and the **OpenAI Agents SDK**.  
- Use **Chainlit** to create an interactive web interface for the bot.  
- Connect the Chainlit interface with the agent, enabling the bot to leverage the LLM’s capabilities.  

---
## Setup & Run

```CMD
# 1️⃣ Create & activate virtual environment
uv init assignment_01
cd assignment_01
Activate with: .venv\Scripts\activate


# 2️⃣ Install dependencies
uv add openai-agents
uv add python-decouple
uv add chainlit

# 3️⃣ Add your gemini API key in a .env file

# 4️⃣ Run the Chainlit app
chainlit run main.py
