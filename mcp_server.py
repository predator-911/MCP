# AI Intern Assignment - MCP Server using EduChain
# Author: Lakshya
# Description: Exposes EduChain content generation tools as an MCP-compatible server (local run)

from fastapi import FastAPI, Query
from typing import List
import uvicorn

# ✅ Import actual EduChain tools
from educhain.generator import generate_mcqs, generate_lesson_plan

app = FastAPI(title="EduChain MCP Server")

# ✅ Bonus Tool: Flashcard Generator (custom)
def generate_flashcards(topic: str, count: int = 5):
    return [
        {"term": f"{topic} Term {i+1}", "definition": f"Definition of {topic} Term {i+1}"}
        for i in range(count)
    ]

# ----------------------------------------
# Endpoint: /mcq
@app.get("/mcq")
def get_mcqs(topic: str = Query(...), count: int = Query(5)):
    """
    Generate multiple-choice questions using EduChain.
    """
    try:
        questions = generate_mcqs(topic, count)
        return {
            "tool": "mcq_generator",
            "topic": topic,
            "questions": questions
        }
    except Exception as e:
        return {"error": str(e)}

# ----------------------------------------
# Endpoint: /lesson-plan
@app.get("/lesson-plan")
def get_lesson_plan(subject: str = Query(...)):
    """
    Generate a lesson plan using EduChain.
    """
    try:
        plan = generate_lesson_plan(subject)
        return {
            "tool": "lesson_plan",
            "subject": subject,
            "plan": plan
        }
    except Exception as e:
        return {"error": str(e)}

# ----------------------------------------
# Endpoint: /flashcards
@app.get("/flashcards")
def get_flashcards(topic: str = Query(...), count: int = Query(5)):
    """
    Generate flashcards (bonus tool).
    """
    cards = generate_flashcards(topic, count)
    return {
        "tool": "flashcard_generator",
        "topic": topic,
        "cards": cards
    }

# ----------------------------------------
# Run locally
if __name__ == "__main__":
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=5000, reload=True)
