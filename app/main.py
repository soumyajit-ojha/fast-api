"""
The main app of source file
"""

from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")

@app.get("/")
def root():
    """
    the root path
    """
    return {"message": "FastAPI is running!"}
