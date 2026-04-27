from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from urllib.parse import quote, urlencode

from pocketbase.models.record import Record
from pocketbase.services.realtime_service import Callable, MessageData
from pocketbase.services.utils.crud_service import CrudService
from pocketbase.utils import camel_to_snake, validate_token

if TYPE_CHECKING:
    from pocketbase.client import Client


class RecordAuthResponse:
    def __init__(
        self,
        token: str,
        record: Record,
        meta: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        self.token = token
        self.record = record
        self.meta = meta
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def is_valid(self) -> bool:
        pass


@dataclass
class AuthProviderInfo:
    name: str
    display_name: str
    state: str
    auth_url: str
    code_verifier: str
    code_challenge: str
    code_challenge_method: str


@dataclass
class AuthMethodsList:
    username_password: bool
    email_password: bool
    auth_providers: list[AuthProviderInfo]
    only_verified: bool = False


class RecordService(CrudService[Record]):
    collection_id_or_name: str

    def __init__(self, client: Client, collection_id_or_name: str) -> None:
        super().__init__(client)
        self.collection_id_or_name = collection_id_or_name

    def decode(self, data: dict[str, Any]) -> Record:
        return Record(data)

    def base_crud_path(self) -> str:
        pass

    def update(
        self,
        id: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> Record:
        """
        If the current `client.auth_store.model` matches with the updated id, then
        on success the `client.auth_store.model` will be updated with the result.
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

    def base_collection_path(self) -> str:
        """Returns the current collection service base path."""
        pass

    def subscribe(self, callback: Callable[[MessageData], None]) -> None:
        """Subscribe to realtime changes of any record from the collection."""
        pass

    def unsubscribe(self, *record_ids: str) -> None:
        """Unsubscribe to the realtime changes of a single record in the collection."""
        pass

    # TODO: add deprecated decorator
    def subscribeOne(
        self, record_id: str, callback: Callable[[MessageData], None]
    ) -> None:
        """Subscribe to the realtime changes of a single record in the collection."""
        pass

    # TODO: add deprecated decorator
    def get_file_url(
        self, record: Record, filename: str, query_params: dict[str, Any] = {}
    ) -> str:
        """Builds and returns an absolute record file url."""
        pass

    # ------------
    # Auth handers
    # ------------

    def auth_response(
        self, response_data: dict[str, Any]
    ) -> RecordAuthResponse:
        """Prepare successful collection authorization response."""
        pass

    def list_auth_methods(
        self, query_params: dict[str, Any] | None = None
    ) -> AuthMethodsList:
        """Returns all available collection auth methods."""
        pass

    def auth_with_password(
        self,
        username_or_email: str,
        password: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> RecordAuthResponse:
        """
        Authenticate a single auth collection record via its username/email and password.

        On success, this method also automatically updates
        the client's AuthStore data and returns:
        - the authentication token
        - the authenticated record model
        """
        pass

    def auth_with_oauth2(
        self,
        provider: str,
        code: str,
        code_verifier: str,
        redirect_url: str,
        create_data: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> RecordAuthResponse:
        """
        Authenticate a single auth collection record with OAuth2.

        On success, this method also automatically updates
        the client's AuthStore data and returns:
        - the authentication token
        - the authenticated record model
        - the OAuth2 account data (eg. name, email, avatar, etc.)
        """
        pass

    def auth_refresh(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> RecordAuthResponse:
        """
        Refreshes the current authenticated record instance and
        returns a new token and record data.

        On success this method also automatically updates the client's AuthStore.
        """
        pass

    def request_email_change(
        self,
        newEmail: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Asks to change email of the current authenticated record instance the new address
        receives an email with a confirmation token that needs to be confirmed with confirmEmailChange()
        """
        pass

    def confirm_email_change(
        self,
        token: str,
        password: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Confirms Email Change by with the confirmation token and confirm with users password
        """
        pass

    def request_password_reset(
        self,
        email: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Sends auth record password reset request."""
        pass

    def request_verification(
        self,
        email: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Sends email verification request."""
        pass

    def confirm_password_reset(
        self,
        password_reset_token: str,
        password: str,
        password_confirm: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Confirms auth record password reset request"""
        pass

    def confirm_verification(
        self,
        token: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """Confirms email verification request."""
        pass

    # TODO: add deprecated decorator
    def authRefresh(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> RecordAuthResponse:
        """
        Deprecated: Use auth_refresh instead.
        """
        pass

    # TODO: add deprecated decorator
    def requestEmailChange(
        self,
        newEmail: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use request_email_change instead.
        """
        pass

    # TODO: add deprecated decorator
    def confirmEmailChange(
        self,
        token: str,
        password: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use confirm_email_change instead.
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
        Deprecated: Use request_password_reset instead.
        """
        pass

    # TODO: add deprecated decorator
    def requestVerification(
        self,
        email: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use request_verification instead.
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
        Deprecated: Use confirm_password_reset instead.
        """
        pass

    # TODO: add deprecated decorator
    def confirmVerification(
        self,
        token: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        """
        Deprecated: Use confirm_verification instead.
        """
        pass
