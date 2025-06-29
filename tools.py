from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import BaseTool
from typing import Optional
from models import llm  # Ensure llm is correctly defined in models.py


class BloodTestTool(BaseTool):
    name: str = "Read Blood Report Tool"
    description: str = "Extract and parse key biomarkers from a blood test report PDF."

    def _run(self, file_path: str) -> str:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        content = "\n".join([page.page_content for page in pages])
        return content

    def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not implemented for BloodTestTool")


class SearchTool(BaseTool):
    name: str = "General Search Tool"
    description: str = "Searches for general medical information using the LLM."
    
    def _run(self, query: str) -> str:
        response = llm.invoke(query)
        return response

    def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not implemented for SearchTool")


# Instantiate tools for agent use
blood_test_tool = BloodTestTool()
search_tool = SearchTool()
