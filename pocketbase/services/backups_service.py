from __future__ import annotations

from typing import Any

from pocketbase.models import Backup, FileUpload
from pocketbase.services.utils import BaseService


class BackupsService(BaseService):
    def decode(self, data: dict[str, Any]) -> Backup:
        return Backup(data)

    def base_path(self) -> str:
        pass

    def create(self, name: str):
        # The backups service create method does not return an object.
        pass

    def get_full_list(self, query_params: dict[str, Any] = {}) -> list[Backup]:
        pass

    def download(self, key: str, file_token: str | None = None) -> bytes:
        pass

    def delete(self, key: str):
        pass

    def restore(self, key: str):
        pass

    def upload(self, file_upload: FileUpload):
        pass
