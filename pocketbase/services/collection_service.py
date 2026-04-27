from __future__ import annotations

from typing import Any

from pocketbase.models.collection import Collection
from pocketbase.services.utils.crud_service import CrudService


class CollectionService(CrudService[Collection]):
    def decode(self, data: dict[str, Any]) -> Collection:
        return Collection(data)

    def base_crud_path(self) -> str:
        pass

    def import_collections(
        self,
        collections: list[str],
        delete_missing: bool = False,
        query_params: dict[str, Any] = {},
    ) -> bool:
        """
        Imports the provided collections.

        If `delete_missing` is `True`, all local collections and schema fields,
        that are not present in the imported configuration, WILL BE DELETED
        (including their related records data)!
        """
        pass
