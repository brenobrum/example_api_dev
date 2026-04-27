from datetime import datetime
from pydantic import BaseModel


class Author(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
