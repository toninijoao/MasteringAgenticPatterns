import json
from agent import Agent
from functions import sum_numbers, multiply_numbers, subtract_numbers, divide_numbers, power, square_root

with open('schemas.json', 'r') as f:
    tool_schemas = json.load(f)

math_tools = {
    "sum_numbers": sum_numbers,
    "multiply_numbers": multiply_numbers,
    "substract_numbers": substract_numbers,
    "divide_numbers": divide_numbers,
    "power": power,
    "square_root": square_root
}

problem_analyzer = Agent(
    name="problem_analyzer",
    system_prompt=(
        "You are a mathematical problem analyzer. Your job is to:\n"
        "1. Break down complex math problems into clear, sequential steps\n"
        "2. Identify what calculations are needed at each step\n"
        "3. Output a structured plan that another agent can follow to perform calculations\n"
        "4. Do NOT perform the actual calculations - just create the step-by-step plan"
    )
)

calculator_agent = Agent(
    name="calculator_agent",
    system_prompt=(
        "You are a calculator agent. Your job is to:\n" 
        "1. Take a step-by-step calculation plan\n" 
        "2. Execute each calculation using your available math tools\n" 
        "3. Show your work clearly for each step\n" 
        "4. Provide the numerical results in a structured format"
    ),
    tools=math_tools,
    tool_schemas=tool_schemas,
)

solution_presenter = Agent(
    name="solution_presenter",
    system_prompt=(
        "You are a solution presenter. Your job is to:\n" \
        "1. Take calculation results and present them as a complete, educational solution\n" \
        "2. Explain what each step accomplished and why it was necessary\n" \
        "3. Provide the final answer clearly\n" \
        "4. Make the solution easy to understand for someone learning math"
    )
)

complex_problem = """
A rectangular garden is 12 meters long and 8 meters wide.
How much fencing is needed to go around the perimeter?
Also, if grass seed is needed at a rate of 0.25 kg per square meter,
how much grass seed is required for the entire garden?
"""

analysis_messages = [{"role": "user", "content": complex_problem}]

analysis_messages, analysis_output = problem_analyzer.run(analysis_messages)

print(analysis_output)