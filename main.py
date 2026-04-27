from fastapi import FastAPI
from app.application.api.authors import authors_routes
from app.application.api.genres import genres_routes
from app.application.api.movies import movies_routes

import uvicorn

app: FastAPI = FastAPI()

app.include_router(authors_routes)
app.include_router(genres_routes)
app.include_router(movies_routes)

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
