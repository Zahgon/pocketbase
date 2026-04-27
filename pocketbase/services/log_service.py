from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote

from pocketbase.models.log_request import LogRequest
from pocketbase.models.utils.list_result import ListResult
from pocketbase.services.utils.base_service import BaseService
from pocketbase.utils import to_datetime


@dataclass
class HourlyStats:
    total: int
    date: str | datetime.datetime


class LogService(BaseService):
    def get_list(
        self,
        page: int = 1,
        per_page: int = 30,
        query_params: dict[str, Any] = {},
    ) -> ListResult[LogRequest]:
        """Returns paginated logged requests list."""
        pass

    def get(self, id: str, query_params: dict[str, Any] = {}) -> LogRequest:
        """Returns a single logged request by its id."""
        pass

    def get_stats(self, query_params: dict[str, Any] = {}) -> list[HourlyStats]:
        """Returns request logs statistics."""
        pass
