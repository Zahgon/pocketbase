from __future__ import annotations

from typing import Any

from pocketbase.models.utils.base_model import BaseModel
from pocketbase.utils import camel_to_snake


class Record(BaseModel):
    collection_id: str
    collection_name: str
    expand: dict[str, Any]

    def load(self, data: dict[str, Any]) -> None:
        pass

    @classmethod
    def parse_expanded(cls, data: Any):
        pass

    def load_expanded(self) -> None:
        pass
