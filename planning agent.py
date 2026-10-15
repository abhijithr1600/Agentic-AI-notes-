from crewai import Agent, Task, Crew, LLM

llm= LLM(
    model="tinyllama:latest",
    base_url="http://localhost:11434",
    temperature=0
)   

planner = Agent(
    role="planning Agent",
    goal="Break goals into clear, achivable steps",
    backstory="you are good at organizing tasks into plans",
    llm=llm,
    verbose=True
)

planning_task = Task(
    description=(
        "create a 7 day plan to learn python programming"
        "give one practical learning task for each day"
    ),
    expected_output="A clear, numbered 7 day python learning plan",
    agent=planner
)

crew=Crew(
    agents=[planner],
    tasks=[planning_task]   
)

results=crew.kickoff()

print("\nPLanning Agent output:")
print(result)