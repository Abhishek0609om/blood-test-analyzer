from models import AgentFactory
from tools import blood_test_tool, search_tool

# Create the factory
factory = AgentFactory()

# Create agents with tools and delegation settings
doctor = factory.create_doctor(
    tools=[blood_test_tool, search_tool],
    allow_delegation=True
)

verifier = factory.create_verifier(
    tools=[blood_test_tool],
    allow_delegation=True
)

nutritionist = factory.create_nutritionist(
    tools=[blood_test_tool, search_tool],
    allow_delegation=False
)

exercise_specialist = factory.create_exercise_specialist(
    tools=[blood_test_tool, search_tool],
    allow_delegation=False
)
