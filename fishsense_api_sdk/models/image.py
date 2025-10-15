from datetime import datetime

from pydantic import BaseModel


class Dive(BaseModel):
    """Model representing an image."""

    id: int | None
    path: str
    taken_datetime: datetime
    checksum: str
    is_canonical: bool

    dive_id: int | None
    camera_id: int | None
