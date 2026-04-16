#  AI Resume Screening System

An AI-powered Resume Screening System that evaluates resumes against job descriptions using **LangChain + Groq LLMs**.

The system follows a **modular multi-chain architecture** to make the pipeline clean, scalable, and production-ready.


##  Objective

To automate resume screening by:
- Extracting key information from resumes
- Matching resumes with job descriptions
- Scoring candidate suitability
- Generating final human-readable evaluation reports

##  System Architecture

This project is built using **4 core chains**:

###  Extraction Chain
- Extracts skills, experience, tools, and education from resumes

### Matching Chain
- Compares resume data with job description
- Finds relevance and alignment

###  Scoring Chain
- Generates final score (0–100)
- Classifies candidate (Strong / Average / Weak)

###  Explanation Chain
- Produces final AI-generated evaluation report
- Lists strengths and weaknesses


##  Project Structure
ai-resume-screening/
│
├── main.py
│
├── chains/
│ ├── extraction_chain.py
│ ├── matching_chain.py
│ ├── scoring_chain.py
│ ├── explanation_chain.py
│
├── prompts/
│ ├── extraction_prompt.py
│ ├── matching_prompt.py
│ ├── scoring_prompt.py
│ ├── explanation_prompt.py
│
├── data/
│ ├── job_description.txt
│ ├── resume_strong.txt
│ ├── resume_average.txt
│ ├── resume_weak.txt
│
├── .env
├── requirements.txt
└── README.md


---

##  Workflow


Resume Input
↓
Extraction Chain → Extract skills & experience
↓
Matching Chain → Compare with job description
↓
Scoring Chain → Generate score (0–100)
↓
Explanation Chain → Final evaluation report
↓
Output → Ranked Candidate Result



##  Tech Stack

- Python 
- LangChain 
- Groq API  (Llama 3)
- python-dotenv 
- LangSmith

## Windows
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
Environment Variables

## Create a .env file:

GROQ_API_KEY=your_groq_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=ai-resume-screening

## Run Project
python main.py

## Conclusion

This project demonstrates how Large Language Models can be effectively used to automate and improve the resume screening process. By combining LangChain’s modular architecture with Groq’s fast LLM inference, the system provides a structured, scalable, and intelligent approach to candidate evaluation.

It also helped me understand real-world concepts like prompt engineering, chain design, and LLM workflow orchestration, which are essential for building modern AI applications.
