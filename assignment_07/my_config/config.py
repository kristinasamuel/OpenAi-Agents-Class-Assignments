from agents import (RunConfig,OpenAIChatCompletionsModel,)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from tavily import TavilyClient

# Load .env
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")   
gemini_model_name = os.getenv("GEMINI_MODEL_NAME") 
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Create Gemini client
client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url,)
# Use OpenAIChatCompletionsModel to create a model
model = OpenAIChatCompletionsModel(openai_client=client,model=str(gemini_model_name))

config = RunConfig(model=model)

# Initialize Tavily client
tavily_client = TavilyClient(api_key=tavily_api_key)