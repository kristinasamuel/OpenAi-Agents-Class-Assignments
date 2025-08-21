# create tools for different tasks

from agents import function_tool

@function_tool
def Math_Tool(a,b):
    print(">>>>> Math Tool Activated.>>>>>")
    return f"the answer of {a} + {b} is: {a + b}"


@function_tool
def Weather_Tool(city):
    print(">>>>>> Weather Tool Activated >>>>>>")
    return f"The weather in {city} is cloudy with a temperature of 27°C." 

@function_tool
def get_latest_news():
    print(">>>>> News Tool Activated.>>>>>")
    return "Latest news: OpenAI releases new AI model that can understand and generate human-like text."