from crewai import Task
from agents import verifier, doctor, nutritionist, exercise_specialist  # Correct import
from tools import search_tool, blood_test_tool  # Use instantiated tools

# Task to verify the blood report
verification = Task(
    description="Verify that the uploaded file at {file_path} is a valid blood test report. "
                "Extract key biomarkers (e.g., cholesterol, glucose, hemoglobin) and summarize them for analysis. "
                "If the file is not a blood report, return an error message. "
                "User query: {query}",
    expected_output="A summary of the blood test report, including key biomarkers and their values, or an error if the file is invalid.",
    agent=verifier,
    tools=[blood_test_tool],  # Fixed here
    async_execution=False,
)

# Task to help solve user's query
help_patients = Task(
    description="Analyze the blood test report at {file_path} and respond to the user's query: {query}. "
                "Provide clear, evidence-based medical advice based on the report data. "
                "Use search_tool to find reliable medical information if needed.",
    expected_output="A detailed response addressing the user's query, including: "
                    "- Summary of relevant blood test results "
                    "- Evidence-based medical advice "
                    "- Clear explanations in plain language",
    agent=doctor,
    tools=[blood_test_tool, search_tool],  # Fixed here
    async_execution=False,
)

# Nutrition analysis task
nutrition_analysis = Task(
    description="Analyze the blood test report at {file_path} and provide personalized nutrition advice based on the user's query: {query}. "
                "Focus on biomarkers relevant to nutrition (e.g., vitamin D, iron). "
                "Use search_tool to find evidence-based dietary recommendations.",
    expected_output="A nutrition plan including: "
                    "- Key biomarkers affecting diet "
                    "- Recommended foods and nutrients "
                    "- Evidence-based sources or reasoning",
    agent=nutritionist,
    tools=[blood_test_tool, search_tool],  # Fixed here
    async_execution=False,
)

# Exercise planning task
exercise_planning = Task(
    description="Analyze the blood test report at {file_path} and design a safe exercise plan based on the user's query: {query}. "
                "Consider biomarkers like hemoglobin or glucose that may affect exercise capacity. "
                "Use search_tool for evidence-based fitness guidelines.",
    expected_output="A personalized exercise plan including: "
                    "- Recommended exercises tailored to the user's health status "
                    "- Safety precautions based on blood test results "
                    "- Evidence-based sources or reasoning",
    agent=exercise_specialist,
    tools=[blood_test_tool, search_tool],  # Fixed here
    async_execution=False,
)
