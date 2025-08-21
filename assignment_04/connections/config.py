#  configuration to set the client and model

from agents import OpenAIChatCompletionsModel,set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(True)

# get the environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key = gemini_api_key , base_url=gemini_base_url)
model = OpenAIChatCompletionsModel(openai_client= client , model =str(gemini_model_name))

