from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from urllib.parse import quote

from pocketbase.errors import ClientResponseError
from pocketbase.models.utils.base_model import Model
from pocketbase.models.utils.list_result import ListResult
from pocketbase.services.utils.base_service import BaseService

T = TypeVar("T", bound=Model)


class CrudService(Generic[T], BaseService, ABC):
    @abstractmethod
    def base_crud_path(self) -> str:
        """Base path for the crud actions (without trailing slash, eg. '/admins')."""

    @abstractmethod
    def decode(self, data: dict[str, Any]) -> T:
        """Response data decoder"""

    def get_full_list(
        self,
        batch: int = 100,
        query_params: dict[str, Any] | None = None,
    ) -> list[T]:
        pass

    def get_list(
        self,
        page: int = 1,
        per_page: int = 30,
        query_params: dict[str, Any] | None = None,
    ) -> ListResult[T]:
        pass

    def get_one(
        self,
        id: str,
        query_params: dict[str, Any] | None = None,
    ) -> T:
        pass

    def get_first_list_item(
        self,
        filter: str,
        query_params: dict[str, Any] | None = None,
    ):
        """
        Returns the first found item by the specified filter.

        Internally it calls `getList(1, 1, { filter })` and returns the
        first found item.

        For consistency with `getOne`, this method will throw a 404
        ClientResponseError if no item was found.
        """
        pass

    def create(
        self,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> T:
        pass

    def update(
        self,
        id: str,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
    ) -> T:
        pass

    def delete(
        self,
        id: str,
        query_params: dict[str, Any] | None = None,
    ) -> bool:
        pass
