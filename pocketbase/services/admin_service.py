from __future__ import annotations

from typing import Any

from pocketbase.models.admin import Admin
from pocketbase.services.utils.crud_service import CrudService
from pocketbase.utils import validate_token


class AdminAuthResponse:
    token: str
    admin: Admin

    def __init__(self, token: str, admin: Admin, **kwargs: Any) -> None:
        self.token = token
        self.admin = admin
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def is_valid(self) -> bool:
        pass


class AdminService(CrudService[Admin]):
    def decode(self, data: dict[str, Any]) -> Admin:
        return Admin(data)

    def base_crud_path(self) -> str:
        pass

    def update(
        self,
        id: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> Admin:
        """
        If the current `client.auth_store.model` matches with the updated id,
        then on success the `client.auth_store.model` will be updated with the result.
        """
        pass

    def delete(
        self, id: str, query_params: dict[str, Any] | None = None
    ) -> bool:
        """
        If the current `client.auth_store.model` matches with the deleted id,
        then on success the `client.auth_store` will be cleared.
        """
        pass

    def auth_response(self, response_data: dict[str, Any]) -> AdminAuthResponse:
        """Prepare successful authorize response."""
        pass

    def auth_with_password(
        self,
        email: str,
        password: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> AdminAuthResponse:
        """
        Authenticate an admin account with its email and password
        and returns a new admin token and data.

        On success this method automatically updates the client's AuthStore data.
        """
        pass

    def auth_refresh(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> AdminAuthResponse:
        """
        Refreshes the current admin authenticated instance and
        returns a new token and admin data.

        On success this method automatically updates the client's AuthStore data.
        """
        pass

    def request_password_reset(
        self,
        email: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Sends admin password reset request."""
        pass

    def confirm_password_reset(
        self,
        password_reset_token: str,
        password: str,
        password_confirm: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Confirms admin password reset request."""
        pass

    # TODO: add deprecated decorator
    def authRefresh(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> AdminAuthResponse:
        """
        Deprecated: Use `auth_refresh` instead.
        """
        pass

    # TODO: add deprecated decorator
    def requestPasswordReset(
        self,
        email: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use `request_password_reset` instead.
        """
        pass

    # TODO: add deprecated decorator
    def confirmPasswordReset(
        self,
        password_reset_token: str,
        password: str,
        password_confirm: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use `confirm_password_reset` instead.
        """
        pass
