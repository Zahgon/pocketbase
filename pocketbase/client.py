from __future__ import annotations

from typing import Any, Dict

import httpx

from pocketbase.errors import ClientResponseError
from pocketbase.models import FileUpload
from pocketbase.models.record import Record
from pocketbase.services.admin_service import AdminService
from pocketbase.services.backups_service import BackupsService
from pocketbase.services.collection_service import CollectionService
from pocketbase.services.files_service import FileService
from pocketbase.services.health_service import HealthService
from pocketbase.services.log_service import LogService
from pocketbase.services.realtime_service import RealtimeService
from pocketbase.services.record_service import RecordService
from pocketbase.services.settings_service import SettingsService
from pocketbase.stores.base_auth_store import AuthStore, BaseAuthStore


class Client:
    def __init__(
        self,
        base_url: str = "/",
        lang: str = "en-US",
        auth_store: AuthStore | None = None,
        timeout: float = 120,
        http_client: httpx.Client | None = None,
        auto_snake_case: bool = True,
    ) -> None:
        self.base_url = base_url
        self.lang = lang
        self.auth_store = auth_store or BaseAuthStore()  # LocalAuthStore()
        self.timeout = timeout
        self.http_client = http_client or httpx.Client()
        self.auto_snake_case = auto_snake_case
        # services
        self.admins = AdminService(self)
        self.backups = BackupsService(self)
        self.collections = CollectionService(self)
        self.files = FileService(self)
        self.health = HealthService(self)
        self.logs = LogService(self)
        self.settings = SettingsService(self)
        self.realtime = RealtimeService(self)
        self.record_service: Dict[str, RecordService] = {}

    def _send(self, path: str, req_config: dict[str, Any]) -> httpx.Response:
        """Sends an api http request returning response object."""
        pass

    def collection(self, id_or_name: str) -> RecordService:
        """Returns the RecordService associated to the specified collection."""
        pass

    def send_raw(self, path: str, req_config: dict[str, Any]) -> bytes:
        """Sends an api http request returning raw bytes response."""
        pass

    def send(self, path: str, req_config: dict[str, Any]) -> Any:
        """Sends an api http request."""
        pass

    def build_url(self, path: str) -> str:
        pass

    # TODO: add deprecated decorator
    def get_file_url(
        self,
        record: Record,
        filename: str,
        query_params: dict[str, Any] | None = None,
    ):
        pass

    # TODO: add deprecated decorator
    def get_file_token(self) -> str:
        pass
