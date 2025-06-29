from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

class AgentFactory:
    def __init__(self):
        self.llm = llm

    def create_doctor(self, tools, allow_delegation):
        return Agent(
            role="Senior Doctor",
            goal="Interpret and explain the blood test results",
            backstory="Expert in diagnostics and internal medicine.",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation
        )

    def create_verifier(self, tools, allow_delegation):
        return Agent(
            role="Medical Data Verifier",
            goal="Ensure accuracy of extracted test values and flag anomalies",
            backstory="Highly experienced in laboratory test validation.",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation
        )

    def create_nutritionist(self, tools, allow_delegation):
        return Agent(
            role="Certified Nutritionist",
            goal="Provide dietary suggestions based on blood report",
            backstory="Expert in nutritional therapy and metabolism.",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation
        )

    def create_exercise_specialist(self, tools, allow_delegation):
        return Agent(
            role="Fitness and Exercise Specialist",
            goal="Suggest personalized exercises based on health condition",
            backstory="Background in physiotherapy and sports science.",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation
        )
