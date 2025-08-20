# my_connections/config.py
# set configuration to run agent

from agents import OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

set_tracing_disabled(True)
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name= os.getenv("GEMINI_MODEL_NAME")

gemini_client = AsyncOpenAI(api_key=gemini_api_key , base_url= gemini_base_url,)
model = OpenAIChatCompletionsModel(openai_client=gemini_client,model=str(gemini_model_name))
