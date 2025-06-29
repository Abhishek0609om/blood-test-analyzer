# 🧪 Blood Test Report Analyzer

A modular, FastAPI-based backend that leverages **CrewAI**, **LangChain**, and **OpenAI** to intelligently analyze PDF blood test reports. It returns actionable, ethical, and accurate insights from four virtual specialists:
- 👨‍⚕️ Doctor  
- ✅ Medical Verifier  
- 🍎 Nutritionist  
- 🏃‍♂️ Exercise Coach  

---

## 🐞 Bugs Found and Fixed

This project initially contained serious technical and ethical issues. All have been identified and professionally resolved.

### 🔧 Technical Fixes

| Issue | Original Problem | Fix Applied |
|-------|------------------|-------------|
| ❌ Broken LLM Initialization | `llm = llm` was a placeholder that broke runtime | ✅ Proper LLM initialization using OpenAI API key from `.env` |
| ❌ Async Misuse | `read_data_tool` marked as async but never awaited | ✅ Wrapped in async function and correctly awaited |
| ❌ Missing Import | `PDFLoader` not imported | ✅ Imported from `langchain.document_loaders` |
| ❌ Duplicate PDFs | Both `sample.pdf` and `blood_test_report.pdf` had identical content | ✅ Kept one standardized sample and deleted the duplicate |
| ❌ No Quota Handling | App crashed silently on OpenAI quota exceed | ✅ Added `RateLimitError` handler with clear user guidance |
| ❌ File Name Collisions | File uploads could overwrite each other | ✅ Used `uuid4()` to generate unique filenames |
| ❌ Dependency Conflicts | Installing `crewai`, `openai`, `langchain` together caused errors | ✅ Fixed by version pinning in `requirements.txt` and using two-step install |

---
📦 requirements.txt Notes
The original file had critical conflicts:
❌ Incompatible versions of protobuf, pydantic, google-api-core
❌ crewai, langchain, and openai were unstable together

### ⚖️ Ethical & Design Improvements

| Problem | Original Design | Ethical Fix |
|---------|------------------|-------------|
| ❌ Fake Health Advice | Agents hallucinated diseases and added fake URLs | ✅ Refactored all agents for ethical, real-world-safe outputs |
| ❌ Ignored User Prompts | Task instructions told agents to skip user input | ✅ Now every agent respects user queries and context |
| ❌ Misleading Roles | “Medical Verifier” and others did nothing useful | ✅ All roles now have defined, grounded purposes |
| ❌ Random Reference Links | Hallucinated links to fake studies | ✅ All links and claims removed unless verified |
| ❌ Miscommunication Between Agents | Tools didn’t transfer data properly | ✅ Rewritten tool-agent interface for clean data flow |

---


### 1. Clone the Repository

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

If you face version conflicts:
pip install --no-deps -r requirements.txt
pip install -r requirements.txt

5. Set Your OpenAI API Key
Create a .env file:
OPENAI_API_KEY=your-api-key-here

6. Run the Server
uvicorn main:app --reload

API Usage
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.pdf;type=application/pdf' \
  -F 'query=Summarize my Blood Test Report
  
  Final Notes
This refactored app now follows:
✅ Clean and modular design
✅ Secure and ethical AI usage
✅ Production-grade FastAPI practices
✅ Helpful error handling and user messaging

✍️ Authors & Credits
Refactored and debugged by Abhishek B
As part of an internship evaluation challenge.
Stack: FastAPI • OpenAI • CrewAI • LangChain



