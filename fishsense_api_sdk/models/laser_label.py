from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel


class LaserLabel(BaseModel):
    """Model representing a laser label."""

    id: int | None
    label_studio_task_id: int | None
    x: float | None
    y: float | None
    label: str | None
    updated_at: datetime | None
    completed: bool | None
    label_studio_json: Dict[str, Any] | None

    image_id: int | None
    user_id: int | None
