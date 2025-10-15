from typing import List

from pydantic import BaseModel


class DiveFrameCluster(BaseModel):
    """Model representing a cluster of frames within a dive."""

    id: int
    image_ids: List[int]
