from langchain.agents import create_agent 
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchResults

llm = ChatOllama(
    model="tinyllama:latest",
    temperature=0
)
search_tool = DuckDuckGoSearchResults()
agent=create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt=(
        "you are an autonomous research agent"
        " understand the user's goal, search for useful information"
        " when needed, and prepare a clear summary"
    )
)

result = agent.invoke({
    "message":[
        {
            "role":"user",
            "content":(
                "Research three applications of ai in education"
                "and prepare a short report"
            )
        }
    ]
})

