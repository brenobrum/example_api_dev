from datetime import datetime
from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    name: str
    description: str
    author_id: str
    genre_id: str
    created_at: datetime
    updated_at: datetime
