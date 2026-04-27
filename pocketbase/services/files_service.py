from __future__ import annotations

from typing import Any
from urllib.parse import quote, urlencode

from pocketbase.models.record import Record
from pocketbase.services.utils import BaseService


class FileService(BaseService):
    def get_url(
        self,
        record: Record,
        filename: str,
        query_params: dict[str, Any] | None = None,
    ):
        pass

    def get_token(self) -> str:
        pass
