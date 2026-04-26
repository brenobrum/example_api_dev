from fastapi import FastAPI
from app.application.api.genres import genres_routes

import uvicorn

app: FastAPI = FastAPI()

app.include_router(genres_routes)

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
