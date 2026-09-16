from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
import os
import psycopg
from fastapi.middleware.cors import CORSMiddleware


load_dotenv(Path(__file__).resolve().parent.parent / ".env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status":"ok"}


@app.get("/db-health")
def db_health():
    try:
        with psycopg.connect(os.getenv("DATABASE_URL")) as conn:
            return {"database":"connected"}
    except Exception as e:
        return {"database":"connection failed","error":str(e)}