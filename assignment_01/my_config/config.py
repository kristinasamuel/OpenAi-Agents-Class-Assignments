# configuration file
# set the configuration for gemini api key  

from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

my_key = config("GEMINI_API_KEY")
client = AsyncOpenAI(api_key=my_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
