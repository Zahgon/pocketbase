from __future__ import annotations

from typing import Any

from pocketbase.services.utils.base_service import BaseService


class SettingsService(BaseService):
    def get_all(
        self, query_params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Fetch all available app settings."""
        pass

    def update(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Bulk updates app settings."""
        pass

    def test_s3(self, query_params: dict[str, Any] | None = None) -> bool:
        """Performs a S3 storage connection test."""
        pass

    def test_email(
        self,
        to_email: str,
        email_template: str,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Sends a test email.

        The possible `email_template` values are:
        - verification
        - password-reset
        - email-change
        """
        pass

    def generate_apple_client_secret(
        self,
        client_id: str,
        team_id: str,
        key_id: str,
        private_key: str,
        duration: int,
        query_params: dict[str, Any] | None = None,
    ) -> str:
        pass
