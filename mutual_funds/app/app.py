from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = FastAPI()

@app.route("/")
def home():
    return {"message": "Environment variables are loaded!"}
