from __future__ import annotations

from typing import Any

from pocketbase.models.utils.base_model import BaseModel


class Admin(BaseModel):
    avatar: int
    email: str

    def load(self, data: dict[str, Any]) -> None:
        pass
