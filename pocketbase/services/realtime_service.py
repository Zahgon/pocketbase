from __future__ import annotations

import dataclasses
import json
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from pocketbase.models.record import Record
from pocketbase.services.utils.base_service import BaseService
from pocketbase.services.utils.sse import Event, SSEClient

if TYPE_CHECKING:
    from pocketbase.client import Client


@dataclasses.dataclass
class MessageData:
    action: str
    record: Record


class RealtimeService(BaseService):
    subscriptions: dict[str, Callable[[Any], None]]
    client_id: str = ""
    event_source: SSEClient | None = None

    def __init__(self, client: Client) -> None:
        super().__init__(client)
        self.subscriptions = {}
        self.client_id = ""
        self.event_source = None

    def subscribe(
        self, subscription: str, callback: Callable[[MessageData], None]
    ) -> None:
        """Inits the sse connection (if not already) and register the subscription."""
        pass

    def unsubscribe_by_prefix(self, subscription_prefix: str):
        """
        Unsubscribe from all subscriptions starting with the provided prefix.

        This method is no-op if there are no active subscriptions with the provided prefix.

        The related sse connection will be autoclosed if after the
        unsubscribe operation there are no active subscriptions left.
        """
        pass

    def unsubscribe(self, subscriptions: list[str] | None = None) -> None:
        """
        Unsubscribe from a subscription.

        If the `subscriptions` argument is not set,
        then the client will unsubscribe from all registered subscriptions.

        The related sse connection will be autoclosed if after the
        unsubscribe operations there are no active subscriptions left.
        """
        pass

    def _make_subscription(
        self, callback: Callable[[MessageData], None]
    ) -> Callable[[Event], None]:
        pass

    def _submit_subscriptions(self) -> bool:
        pass

    def _add_subscription_listeners(self) -> None:
        pass

    def _remove_subscription_listeners(self) -> None:
        pass

    def _connect_handler(self, event: Event) -> None:
        pass

    def _connect(self) -> None:
        pass

    def _disconnect(self) -> None:
        pass
