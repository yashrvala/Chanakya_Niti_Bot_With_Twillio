from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import AzureChatOpenAI
from langchain.agents.agent_types import AgentType
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# DuckDuckGo Tool
search = DuckDuckGoSearchRun()

# Azure OpenAI LLM
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Use this tool ONLY to search for topics related to Chanakya Niti. Do NOT search for topics unrelated to Chanakya Niti."
    )
]

# ✅ Initialize the agent with handle_parsing_errors=True
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={
        "prefix": (
            "You are an expert in Chanakya Niti. Answer all questions strictly within the context of Chanakya Niti only. "
            "If the question is outside the scope of Chanakya Niti or ancient Indian wisdom, politely refuse to answer. "
            "Do not hallucinate or make up information beyond this scope."
        )
    }
)

# ✅ Use `invoke` to get response safely
query = "Who is the Prime Minister of India according to Chanakya Niti?"
response = agent.invoke({"input": query})
print(response)
