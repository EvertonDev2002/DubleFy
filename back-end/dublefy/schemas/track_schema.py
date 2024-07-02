from datetime import datetime

from pydantic import BaseModel


class Track(BaseModel):
    id: str
    name: str
    artist: str
    added_at: datetime


class TracksResponse(BaseModel):
    tracks: list[Track]
