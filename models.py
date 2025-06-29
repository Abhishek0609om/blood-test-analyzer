from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo") 

class AgentFactory:
    """Centralized factory for creating medical analysis agents with consistent LLM configuration"""
    
    def __init__(self):
        self.llm = llm  # Shared LLM instance for all agents

    def create_doctor(self, tools, allow_delegation=True):
        """Hematology specialist for interpreting bloodwork"""
        return Agent(
            role="Senior Doctor",
            goal="Interpret and explain the blood test results",  # Focus on clinical analysis
            backstory="Expert in diagnostics and internal medicine with 10+ years experience",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation  # Can delegate to specialists
        )

    def create_verifier(self, tools, allow_delegation=False):
        """Quality control for test result validation"""
        return Agent(
            role="Medical Data Verifier",
            goal="Ensure accuracy of extracted test values",  # Data integrity focus
            backstory="Lab technician specialized in result validation",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation  # Verification shouldn't be delegated
        )

    def create_nutritionist(self, tools, allow_delegation=False):
        """Dietary recommendations based on biomarkers"""
        return Agent(
            role="Certified Nutritionist",
            goal="Provide dietary suggestions",  # Food-first approach
            backstory="Registered dietitian with clinical nutrition specialization",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation  # Independent recommendations
        )

    def create_exercise_specialist(self, tools, allow_delegation=False):
        """Safe exercise planning considering blood results"""
        return Agent(
            role="Exercise Physiologist",
            goal="Suggest personalized exercises",  # Safety-focused
            backstory="Physical therapist with sports medicine background",
            tools=tools,
            llm=self.llm,
            allow_delegation=allow_delegation  # Direct recommendations
        )