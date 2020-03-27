from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    title: str
    url: str


class Edition(BaseModel):
    title: str
    description: str
    type: int
    publisher_id: int
    texts: list
    images: List[Image]
    youtube_videos: list
