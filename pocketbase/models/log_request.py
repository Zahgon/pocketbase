from __future__ import annotations

from typing import Any

from pocketbase.models.utils.base_model import BaseModel


class LogRequest(BaseModel):
    url: str
    method: str
    status: int
    auth: str
    remote_ip: str
    user_ip: str
    referer: str
    user_agent: str
    meta: dict[str, Any]

    def load(self, data: dict[str, Any]) -> None:
        pass
