#  Guardrials input and ouput

from agents import RunContextWrapper,input_guardrail,GuardrailFunctionOutput,Agent,Runner,output_guardrail
from my_schema.schema import PoliticalSchema
from my_connections.connect import model

guardrial_agent = Agent(
    name = "Guardrial Agent",
    instructions="You are a guardrail agent. Check if the user query is about Math or not.",
    model = model,
    output_type = PoliticalSchema
)
@input_guardrail
async def guardrial_input_function(ctx:RunContextWrapper,agent,input ):
    result = await Runner.run(guardrial_agent, input = input , context = ctx.context)
    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered = not result.final_output.is_math_question
    )

@output_guardrail
async def guardrail_output_function(ctx: RunContextWrapper, agent, output):
    result = await Runner.run(guardrial_agent, input=output, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_political_question
    )
