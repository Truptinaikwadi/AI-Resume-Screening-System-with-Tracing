from chains.explanation_chain import explanation_chain
from chains.scoring_chain import scoring_chain
from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain   # <-- missing import

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ai-resume-screening"

# ---------- Read single file ----------
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ---------- Process one resume ----------
def process_resume(resume_path, job):
    print(f"\n🔍 Processing: {resume_path}")

    # Step 1: Read resume
    resume = read_file(resume_path)

    # Step 2: Extraction
    extracted = extraction_chain(resume)
    print("\n📌 Extracted:\n", extracted)

    # Step 3: Matching
    matched = matching_chain(job, extracted)
    print("\n🔗 Matching:\n", matched)

    # Step 4: Scoring
    score = scoring_chain(matched)
    print("\n📊 Score:\n", score)

    # Step 5: Explanation
    explanation = explanation_chain({
        "score": score,
        "matching_data": matched
    })
    print("\n🧠 Explanation:\n", explanation)

    return score


# ---------- MAIN ----------
if __name__ == "__main__":

    # read job description
    job = read_file("data/job_description.txt")

    # list of resumes
    resumes = [
        "data/resume_strong.txt",
        "data/resume_average.txt",
        "data/resume_weak.txt"
    ]

    # process all resumes
    results = {}

    for resume_path in resumes:
        score = process_resume(resume_path, job)
        results[resume_path] = score

    print("\n====================")
    print("FINAL SCORES")
    print("====================")

    for k, v in results.items():
        print(f"{k} ➜ {v}")