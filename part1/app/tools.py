from langchain.tools import Tool
from sympy import sympify

def calculator_tool(input: str) -> str:
    try:
        expression = sympify(input)
        result = expression.evalf()
        return str(result)
    except Exception as e:
        return f"Error: Invalid expression – {str(e)}"

calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Use this to solve math problems like '15 * 7' or '3 + 5 / 2'."
)
