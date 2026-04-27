from __future__ import annotations

from typing import Any

from pocketbase.models.utils.base_model import BaseModel
from pocketbase.models.utils.collection_field import CollectionField


class Collection(BaseModel):
    name: str
    type: str
    fields: list[CollectionField]
    system: bool
    list_rule: str | None
    view_rule: str | None
    create_rule: str | None
    update_rule: str | None
    delete_rule: str | None
    options: dict[str, Any]

    def load(self, data: dict[str, Any]) -> None:
        pass

    def is_base(self):
        pass

    def is_auth(self):
        pass

    def is_single(self):
        pass
