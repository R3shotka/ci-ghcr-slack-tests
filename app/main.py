from fastapi import FastAPI, Query
from app.utils import add
from app.db import ping_db

app = FastAPI(title="CI Demo API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sum")
def sum_endpoint(a: int = Query(...), b: int = Query(...)):
    return {"result": add(a, b)}

@app.get("/db/health")
def db_health():
    return {"db_ok": ping_db()}
