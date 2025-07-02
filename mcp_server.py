# AI Intern Assignment - MCP Server using EduChain
# Author: Lakshya

from fastapi import FastAPI, Query
import uvicorn

app = FastAPI(title="EduChain MCP Server (Simulated)")

def generate_mcqs(topic: str, count: int = 5):
    return [
        {
            "question": f"What is {topic} concept #{i+1}?",
            "options": [f"Option A{i}", f"Option B{i}", f"Option C{i}", f"Option D{i}"],
            "answer": f"Option A{i}"
        }
        for i in range(count)
    ]


def generate_lesson_plan(subject: str):
    return {
        "subject": subject,
        "outline": [
            f"Introduction to {subject}",
            f"Core concepts in {subject}",
            f"Activities and examples",
            f"Assessment and summary"
        ]
    }

# ✅ Bonus: Flashcard Generator
def generate_flashcards(topic: str, count: int = 5):
    return [
        {
            "term": f"{topic} Term {i+1}",
            "definition": f"Definition of {topic} Term {i+1}"
        }
        for i in range(count)
    ]

# ----------------------------------------
@app.get("/mcq")
def get_mcqs(topic: str = Query(...), count: int = Query(5)):
    return {
        "tool": "mcq_generator",
        "topic": topic,
        "questions": generate_mcqs(topic, count)
    }

@app.get("/lesson-plan")
def get_lesson_plan(subject: str = Query(...)):
    return {
        "tool": "lesson_plan",
        "subject": subject,
        "plan": generate_lesson_plan(subject)
    }

@app.get("/flashcards")
def get_flashcards(topic: str = Query(...), count: int = Query(5)):
    return {
        "tool": "flashcard_generator",
        "topic": topic,
        "cards": generate_flashcards(topic, count)
    }

# ----------------------------------------
if __name__ == "__main__":
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=5000, reload=True)
