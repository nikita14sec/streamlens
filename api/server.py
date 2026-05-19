from fastapi import FastAPI
from core.engine import Engine

app = FastAPI()
engine = Engine()

@app.post("/query")
def query(payload: dict):
    return engine.run(payload["sql"])
