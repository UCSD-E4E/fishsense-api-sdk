from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel


class SpeciesLabel(BaseModel):
    """Model representing a species label."""

    id: int | None
    label_studio_task_id: int | None
    image_url: str | None
    updated_at: datetime | None
    completed: bool | None
    label_studio_json: Dict[str, Any] | None

    image_id: int | None
    user_id: int | None
