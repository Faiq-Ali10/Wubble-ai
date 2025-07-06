import os
from dotenv import load_dotenv
from tabnanny import verbose
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain.memory import ConversationBufferWindowMemory
from app.tools import calculator

# Set API keys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
SerpAPI = os.getenv("SERPAPI_API_KEY")
GroqAPI = os.getenv("GroqAPI")
os.environ["Groq_API_Key"] = str(GroqAPI)
os.environ["SERPAPI_API_KEY"] = str(SerpAPI)

# Load LLM
llm = ChatGroq(model="llama3-8b-8192", temperature=0.3)

# Load tools
tools = load_tools(["serpapi", "wikipedia"], llm=llm)
tools.append(calculator)

# Load memory
memory = ConversationBufferWindowMemory(k=4, memory_key="chat_history")

# Load system prompt
file_path = os.path.join(os.path.dirname(__file__), "system_prompt.txt")
with open(file_path, "r") as f:
    system_prompt = f.read()

prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "chat_history"],
    template=system_prompt
)

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
)

# Entry function
def run_agent(user_input: str):
    try:
        return agent.run(user_input)
    except Exception as e:
        return f"Error: {str(e)}"
