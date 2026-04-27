from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pocketbase.services.utils import BaseService


@dataclass
class HealthCheckResponse:
    code: int
    message: str
    data: dict[str, Any]


class HealthService(BaseService):
    def check(
        self, query_params: dict[str, Any] | None = None
    ) -> HealthCheckResponse:
        pass
