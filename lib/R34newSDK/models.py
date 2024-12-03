from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


class FilePath(BaseModel):
    url: str
    preview_url: str


class Post(BaseModel):
    id: int
    owner_id: int
    url: str = ""
    file: Union[FilePath, str]
    upload_date: datetime
    type: str
    tags: List[str]
    hash: str
    title: str
    description: str
    source: str
    rating: int
    views: int