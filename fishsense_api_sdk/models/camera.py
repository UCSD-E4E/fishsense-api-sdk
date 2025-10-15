from pydantic import BaseModel


class Camera(BaseModel):
    """Model representing a camera."""

    id: int | None
    serial_number: str
    name: str
