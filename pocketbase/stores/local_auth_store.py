from __future__ import annotations

import os
import pickle
from typing import Any

from pocketbase.models.admin import Admin
from pocketbase.models.record import Record
from pocketbase.stores.base_auth_store import BaseAuthStore


class LocalAuthStore(BaseAuthStore):
    filename: str
    filepath: str

    def __init__(
        self,
        filename: str = "pocketbase_auth.data",
        filepath: str = "",
        base_token: str = "",
        base_model: Record | Admin | None = None,
    ) -> None:
        super().__init__(base_token, base_model)
        self.filename = filename
        self.filepath = filepath
        self.complete_filepath = os.path.join(filepath, filename)

    @property
    def token(self) -> str:
        pass

    @property
    def model(self) -> Record | Admin | None:
        pass

    def save(
        self, token: str = "", model: Record | Admin | None = None
    ) -> None:
        pass

    def clear(self) -> None:
        pass

    def _storage_set(self, key: str, value: Any) -> None:
        pass

    def _storage_get(self, key: str) -> Any:
        pass

    def _storage_remove(self, key: str) -> None:
        pass
